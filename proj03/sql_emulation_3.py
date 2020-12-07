import sqlite3
def use_connection(conn):
  c = conn.cursor()
  c.execute("SELECT count() FROM students;")
  return c.fetchone()[0]