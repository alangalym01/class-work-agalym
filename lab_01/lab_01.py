from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Lab 1")

Label(root, text='Name').grid(row=0)
input1 = Entry(root)
input1.grid(row=0, column=1)

Label(root, text='Age').grid(row=1)
input2 = Entry(root)
input2.grid(row=1, column=1)

multilingual_status = IntVar()
Checkbutton(root, text='Multilingual', variable=multilingual_status).grid(row=3, sticky=W)

root.mainloop()