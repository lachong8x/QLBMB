
import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('DROP TABLE IF EXISTS devices')
conn.execute('''
    CREATE TABLE devices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        system TEXT NOT NULL,
        status TEXT NOT NULL,
        error_date TEXT,
        progress TEXT
    )
''')

sample_data = [
    ('Thiết bị A', 'Windows', 'Online', '', ''),
    ('Thiết bị B', 'Linux', 'Offline', '', ''),
    ('Thiết bị C', 'macOS', 'Online', '', '')
]

conn.executemany('INSERT INTO devices (name, system, status, error_date, progress) VALUES (?, ?, ?, ?, ?)', sample_data)
conn.commit()
conn.close()
print("Initialized database with sample data.")
