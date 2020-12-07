import datetime
import sqlite3

def convert_to_sql(dict_):
    conn = sqlite3.connect("test.db")
    conn.execute("CREATE TABLE bitcoin (time TEXT, price REAL);")
    for key, price in dict_.items():
        conn.execute("INSERT INTO bitcoin VALUES (?,?);", (key.strftime("%Y-%m-%d %H:%M:%S"), price))
    conn.commit()
    conn.close()