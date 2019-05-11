from tkinter import *

root = Tk()

root.geometry('1000x600')
root.title("A2 System")

label_1 = Label(root, text="Enter Name ", width=20, font=("bold",15))
label_1.place(x=320,y=130)

entry_1 = Entry(root)
entry_1.place(x=550,y=130)

Button(root, text="Start Capture",width=15,bg="brown",fg="white").place(x=450,y=200)

root.mainloop()