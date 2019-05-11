from tkinter import *

root = Tk()

root.geometry('1000x600')
root.title("A2 System")

Button(root, text="View Admission",width=15,bg="brown",fg="white").place(x=450,y=100)
Button(root, text="Training",width=15,bg="blue",fg="white").place(x=450,y=160)
Button(root, text="Exit",width=15,bg="brown",fg="white").place(x=450,y=220)

root.mainloop()