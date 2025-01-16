
CREATE TABLE IF NOT EXISTS historical_figures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    year INTEGER,
    lat REAL,
    lon REAL,
    link TEXT,
    story TEXT
);

INSERT INTO historical_figures (name, year, lat, lon, link, story) VALUES
('Sanni Lemmikki Sjöholm', 1997, 60.1699, 24.9384, '', 'The root of the family tree, born in 1997.'),
('Päivi Lemmikki Sjöholm (Koivunen)', 1966, 60.2, 24.9, '', 'Mother of Sanni Lemmikki Sjöholm, born in 1966.'),
('Esa Antero Sjöholm', 1964, 60.3, 24.8, '', 'Father of Sanni Lemmikki Sjöholm, born in 1964.'),
('Eeva Lemmikki Koivunen (Kause)', 1941, 60.4, 24.7, '', 'Grandmother of Sanni Lemmikki Sjöholm, born in 1941.'),
('Ismo Juhani Koivunen', 1939, 60.5, 24.6, '', 'Grandfather of Sanni Lemmikki Sjöholm, born in 1939.');