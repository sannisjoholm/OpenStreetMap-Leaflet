import sqlite3
import re

# Connect to the database
conn = sqlite3.connect("history.db")
c = conn.cursor()

# Open the text file
file_path = "sukupuu_oma_laajennettu.txt"
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Function to extract data from lines
def extract_data(line):
    match = re.match(r"(\d+)\s([^\(]+)\s\(([\d.]+)\)", line)
    if match:
        generation = int(match.group(1))  # Family tree generation level
        name = match.group(2).strip()     # Person's full name
        birth_date = match.group(3)       # Birth date (DD.MM.YYYY format)
        return generation, name, birth_date
    return None

# Store processed data
family_tree = []
parent_stack = {}  # Stack to track parent-child relationships

for line in lines:
    data = extract_data(line)
    if data:
        generation, name, birth_date = data
        parent_id = parent_stack.get(generation - 1, None)  # Get parent from previous level
        
        # Insert into database
        c.execute("INSERT INTO historical_figures (name, birth_year, parent_id) VALUES (?, ?, ?)", 
                  (name, birth_date.split(".")[-1], parent_id))
        
        # Get inserted row ID and update stack
        person_id = c.lastrowid
        parent_stack[generation] = person_id

# Commit and close
conn.commit()
conn.close()
print("Family tree data successfully inserted into the database!")
