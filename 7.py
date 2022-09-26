from tkinter import *

root = Tk()

def add(event):
    li.insert(0, mes.get())

def sec_add(event):
    mes.insert(0, li.get(ACTIVE))

li = Listbox(height=3)
li.bind('<Double-Button-1>', sec_add)
li.pack(side=LEFT)

mes = StringVar()
mes = Entry(textvariable=mes)
mes.bind('<Return>', add)
mes.pack(side=RIGHT)

root.mainloop()