from tkinter import *
from tkinter import ttk
import sqlite3

root=Tk()

treeV=ttk.Treeview(root,selectmode="extended",columns=('id','Name','Qual','Spec'))

treeV.heading('#0',text="",anchor=CENTER)
treeV.heading('#1',text="ID",anchor=CENTER)
treeV.heading('#2',text="Name",anchor=CENTER)
treeV.heading('#3',text="Qual",anchor=CENTER)
treeV.heading('#4',text="Spec",anchor=CENTER)

treeV.column('#0',width=20)
treeV.column('#1',width=100)
treeV.column('#2',width=100)
treeV.column('#3',width=100)
treeV.column('#4',width=100)
treeV.pack()


conn=sqlite3.connect("new.db")

with conn:
	cur=conn.cursor()
	cur.execute("SELECT * FROM doctor ORDER BY id DESC")

	for row in cur.fetchall():
		treeV.insert('',0,text=row[0],values=(row[0],row[1],row[2],row[3]))

root.mainloop()