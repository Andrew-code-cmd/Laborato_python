from tkinter import *

root = Tk()

var = BooleanVar()
var.set(1)
var2 = BooleanVar()
var2.set(1)
var3 = BooleanVar()
var3.set(1)

l = Label(text="")

def b_b1():
    l['text'] = "Соответствующая информация для Васи"
def b_b2():
    l['text'] = "Соответствующая информация для Пети"
def b_b3():
    l['text'] = "Соответствующая информация для Маши"

l.pack(side=RIGHT)

b1 = Radiobutton(text='Вася', variable=var, command=b_b1, indicatoron=0, width=12, height=2).pack()
b2 = Radiobutton(text='Петя', variable=var2, command=b_b2, indicatoron=0, width=12, height=2).pack()
b3 = Radiobutton(text='Маша', variable=var3, command=b_b3, indicatoron=0, width=12, height=2).pack()



root.mainloop()

