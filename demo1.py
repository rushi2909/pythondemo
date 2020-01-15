from tkinter import *
from tkinter import ttk
import sqlite3

root=Tk()

root.geometry("1200x800")
treeV=ttk.Treeview(root,columns=('one','two','three'),selectmode="extended")

treeV.heading('#0',text='ID',anchor=CENTER)
treeV.heading('#1',text='Name',anchor=CENTER)
treeV.heading('#2',text='Qual',anchor=CENTER)
treeV.heading('#3',text='Spec',anchor=CENTER)

treeV.column('#0',minwidth=20,width=30,stretch=YES)

treeV.column('#1',minwidth=50,width=100,stretch=YES)

treeV.column('#2',minwidth=50,width=100,stretch=YES)

treeV.column('#3',minwidth=50,width=100,stretch=YES)
treeV.pack()

conn=sqlite3.connect("new.db")
with conn:
	cur=conn.cursor()
	cur.execute("select * from doctor")
	for row in cur.fetchall():
		treeV.insert('',0,text=row[0],values=(row[1],row[2],row[3]))


root.mainloop()