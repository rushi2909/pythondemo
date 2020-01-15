import sqlite3
conn=sqlite3.connect("new.db")
with conn:
	cur=conn.cursor()
	cur.execute("insert into doctor(name,qual,spec) values('kedar','BTECH','CSE')")

	cur.execute("insert into doctor(name,qual,spec) values('Saurav','BE','CSE')")

	cur.execute("UPDATE doctor set name='kedar habib' where id=4 ")

print("Record UPDATE")