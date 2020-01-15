from tkinter import *
from tkinter.ttk import *
root=Tk()

def disp():
	label1=Label(root,text=rbstr.get()).place(x=100,y=60)

root.title("Radio Button")
root.geometry("400x400")

rbstr=StringVar()

rb1=Radiobutton(root,text="Male",variable=rbstr,value="Male")
rb2=Radiobutton(root,text="Female",variable=rbstr,value="Female")

rb1.place(x=10,y=20)
rb2.place(x=10,y=40)

btn=Button(root,text="Submit",command=disp)
btn.place(x=10,y=60)




root.mainloop()