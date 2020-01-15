import sqlite3
conn=sqlite3.connect("new.db")

with conn:
	cur=conn.cursor()
	cur.execute("SELECT * FROM doctor")

	for row in cur.fetchall():
		print("id"+str(row[0]))
		print("Name"+str(row[1]))
		print("Qual"+str(row[2]))
		print("Spec"+str(row[3]))
		