How to run server:
```bash
	python server.py
```

after opening server:
http://127.0.0.1:5000
http://127.0.0.1:5000/get_data

run SQLite
```bash
	sqlite3 history.db
```

example how to use sqlite3:
PRAGMA table_info(historical_figures);
ALTER TABLE historical_figures ADD COLUMN birth_year INTEGER;
DELETE FROM table_name WHERE id = value;
.exit