import sqlite3

def crud(conn):
    conn.execute("INSERT INTO students VALUES ('Cam', 98, ''); ")
    conn.execute("UPDATE students SET grade=100 WHERE name='Josh';")
    conn.execute("UPDATE students SET grade=grade-10, notes='SUCKER'  WHERE name LIKE '%z%'")
    conn.execute("DELETE FROM students WHERE grade <= 60")