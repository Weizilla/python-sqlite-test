import sqlite3
conn = sqlite3.connect("straight-sql.db")

c = conn.cursor()
c.execute("""DROP TABLE IF EXISTS person""")
c.execute("""CREATE TABLE person
    (id INTEGER PRIMARY KEY ASC, name VARCHAR(250) NOT NULL)""")
c.execute("""INSERT INTO person VALUES(1, "hello sqlite")""")

conn.commit()
conn.close()

