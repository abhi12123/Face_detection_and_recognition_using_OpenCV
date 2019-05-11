from tkinter import *
import subprocess

root = Tk()

root.geometry('1000x600')
root.title("A2 System")

def exit():
	subprocess.call('python login.py'.split())

def edit():
	subprocess.call('xdg-open images'.split())

def editadmsn():
	subprocess.call('python editadmsn.py'.split())

Button(root, text="New Admission",width=15,bg="brown",fg="white",command=editadmsn).place(x=450,y=100)
Button(root, text="Edit Admission",width=15,bg="brown",fg="white",command=edit).place(x=450,y=160)
Button(root, text="Exit",width=15,bg="brown",fg="white",command=exit).place(x=450,y=220)

root.mainloop()