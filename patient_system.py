import sqlite3

conn = sqlite3.connect("patients.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
symptoms TEXT
)
""")

cursor.execute("INSERT INTO patients (name, age, symptoms) VALUES ('Ali',30,'Fever,Cough')")

conn.commit()

for row in cursor.execute("SELECT * FROM patients"):
    print(row)

conn.close()
