from tkinter import *
import subprocess

Dict = {'admin': 'admin', 'teacher': 'teacher'}


def check():
	username = str(entry_1.get())
	password = str(entry_2.get())
	if Dict[username]==password and password=='teacher':
		subprocess.call('python teacher.py'.split())
	if Dict[username]==password and password=='admin':
		subprocess.call('python admin.py'.split())

root = Tk()

root.geometry('1000x600')
root.title("A2 System")

label_0 = Label(root, text="Login Form", width=20, font=("bold",20))
label_0.place(x=350,y=53)

label_1 = Label(root, text="User Name ", width=20, font=("bold",15))
label_1.place(x=320,y=130)

entry_1 = Entry(root)
entry_1.place(x=550,y=130)


label_2 = Label(root, text="Password ", width=20, font=("bold",15))
label_2.place(x=310,y=180)

entry_2 = Entry(root)
entry_2.place(x=550,y=180)

var = IntVar()
Checkbutton(root, text=" Remember me", variable=var).place(x=540,y=230)

Button(root, text="Submit",width=15,bg="brown",fg="white",command=check).place(x=450,y=260)
root.mainloop()