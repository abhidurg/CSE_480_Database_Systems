import sqlite3
def build_database(filename):
  conn = sqlite3.connect(filename)
  c = conn.cursor()
  c.execute("CREATE TABLE students(name TEXT, points INTEGER)")
  c.execute("INSERT INTO students VALUES ('Josh', 45)")
  c.execute("INSERT INTO students VALUES ('Dennis', 62)")
  c.execute("INSERT INTO students VALUES ('Cam', 42)")
  c.execute("INSERT INTO students VALUES ('Jie', 83)")
  c.execute("INSERT INTO students VALUES ('Zizhen', 92)")
  conn.commit()
  conn.close()