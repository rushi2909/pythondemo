from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()

def login():
	if (e1.get()=="1" and e2.get()=="1"):

		
		root.destroy()
		dashboard=Tk()
		dashboard.title("Dashboard")
		dashboard.geometry("1200x800")

		def sub():
			docName=e4.get()
			docQual=e5.get()
			docSpec=e6.get()

			conn=sqlite3.connect("new.db")

			with conn:
				cur=conn.cursor()

				cur.execute('INSERT INTO doctor(Name,Qual,Spec) VALUES(?,?,?)',(docName,docQual,docSpec))
				msg=messagebox.showinfo("Login Status","Entery Succesful")

				e4.delete(0,END)
				e5.delete(0,END)
				e6.delete(0,END)

		def cls():
			e4.delete(0,END)
			e5.delete(0,END)
			e6.delete(0,END)		

		l3=Label(dashboard,text="Doctor")
		l3.pack()	

		l4=Label(dashboard,text="Name").place(x=520,y=50)
		e4=Entry(dashboard)
		e4.place(x=650,y=50)

		l5=Label(dashboard,text="Qualification").place(x=520,y=80)
		e5=Entry(dashboard)
		e5.place(x=650,y=80)

		l6=Label(dashboard,text="Specialization").place(x=520,y=110)
		e6=Entry(dashboard)
		e6.place(x=650,y=110)

		b2=Button(dashboard,text="Submit",command=sub)
		b2.place(x=540,y=140)

		b4=Button(dashboard,text="Clear",command=cls)
		b4.place(x=600,y=140)

		b5 = Button(dashboard,text="Back")
		b5.place(x=680,y=140)

		dashboard.mainloop()
	else:
		msg=messagebox.showinfo("Login Failed","Enter Deined")
	


root.title("Login page")
root.geometry("400x400")
l1=Label(root,text="Username")
l1.place(x=10,y=20)

l2=Label(root,text="Password")
l2.place(x=10,y=40)

e1=Entry(root)
e1.place(x=80,y=20)

e2=Entry(root,show="*")
e2.place(x=80,y=40)

b1=Button(root,text="Login",command=login)
b1.place(x=60,y=80)

root.mainloop()

