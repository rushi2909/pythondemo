import sqlite3
conn=sqlite3.connect("new.db")
with conn:
	cur=conn.cursor()

	cur.execute("UPDATE doctor set name='kedar habib' where id=4 ")

print("Record UPDATE")