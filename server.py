from flask import Flask, jsonify, request, render_template, send_from_directory
import sqlite3
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to initialize the database
def init_db():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS historical_figures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year INTEGER,
            lat REAL,
            lon REAL,
            link TEXT,
            story TEXT,
            parent_id INTEGER,
            FOREIGN KEY (parent_id) REFERENCES historical_figures(id)
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/get_data", methods=["GET"])
def get_data():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("SELECT id, name, year, lat, lon, link, story, parent_id FROM historical_figures")
    data = [
        {
            "id": row[0],
            "name": row[1],
            "year": row[2],
            "lat": row[3],
            "lon": row[4],
            "link": row[5],
            "story": row[6],
            "parent_id": row[7]
        } for row in c.fetchall()
    ]
    conn.close()
    return jsonify(data)

@app.route("/add_story", methods=["POST"])
def add_story():
    data = request.json
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("INSERT INTO historical_figures (name, year, lat, lon, link, story, parent_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (data["name"], data["year"], data["lat"], data["lon"], data["link"], data["story"], data.get("parent_id")))
    conn.commit()
    conn.close()
    return jsonify({"message": "Story added successfully!"}), 201

@app.route("/update_story", methods=["POST"])
def update_story():
    data = request.json
    conn = sqlite3.connect("history.db")
    c = conn.cursor()
    c.execute("UPDATE historical_figures SET name = ?, year = ?, lat = ?, lon = ?, link = ?, story = ?, parent_id = ? WHERE id = ?",
              (data["name"], data["year"], data["lat"], data["lon"], data["link"], data["story"], data["parent_id"], data["id"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "Story updated successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
