from tkinter import *

root = Tk()

root.geometry('1000x600')
root.title("A2 System")

Button(root, text="Capture",width=15,bg="brown",fg="white").place(x=150,y=100)
Button(root, text="Edit Photos",width=15,bg="brown",fg="white").place(x=150,y=160)
Button(root, text="Train",width=15,bg="blue",fg="white").place(x=150,y=220)

root.mainloop()