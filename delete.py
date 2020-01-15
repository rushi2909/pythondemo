import sqlite3
conn=sqlite3.connect("new.db")
with conn:
	cur=conn.cursor()

	cur.execute("DELETE from doctor where id='8' ")

print("Record DELETEd")