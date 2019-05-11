from tkinter import *
import subprocess

root = Tk()

root.geometry('1000x600')
root.title("A2 System")

def start():
	subprocess.call('python faces.py'.split())

Button(root, text="Start",width=15,bg="brown",fg="white",command=start).place(x=150,y=100)
Button(root, text="Stop",width=15,bg="brown",fg="white").place(x=150,y=160)
Button(root, text="View",width=15,bg="brown",fg="white").place(x=150,y=220)

root.mainloop()