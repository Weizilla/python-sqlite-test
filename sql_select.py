import sqlite3
conn = sqlite3.connect("straight-sql.db")

c = conn.cursor()
c.execute("""SELECT * FROM person""")
print(c.fetchall())

conn.close()
