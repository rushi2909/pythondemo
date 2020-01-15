from tkinter import *
from tkinter import messagebox
root=Tk()

def clr():
	ent1.delete(0,END)
	ent2.delete(0,END)

def login():
	print(ent1.get())
	print(ent2.get())
root.title("Login Form")
root.geometry("400x400")

label1=Label(root,text="Username")
label1.place(x=10,y=20)

ent1=Entry(root)
ent1.place(x=70,y=20)

label2=Label(root,text="Password")
label2.place(x=10,y=50)

ent2=Entry(root,show="*")
ent2.place(x=70,y=50)

btn1=Button(root,text="Login",command=login)
btn1.place(x=30,y=80)

btn2=Button(root,text="clr",command=clr)
btn2.place(x=100,y=80)










root.mainloop()	