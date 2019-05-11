from tkinter import *
import subprocess

root = Tk()

root.geometry('1000x600')
root.title("A2 System")

def exit():
	subprocess.call('python login.py'.split())

def view():
	subprocess.call('libreoffice --calc att.xlsx'.split())

def start():
	subprocess.call('python tchrstart.py'.split())

Button(root, text="Start Attendence",width=15,bg="brown",fg="white",command=start).place(x=450,y=100)
Button(root, text="View Attendence",width=15,bg="brown",fg="white",command=view).place(x=450,y=160)
Button(root, text="Exit",width=15,bg="brown",fg="white",command=exit).place(x=450,y=220)

root.mainloop()