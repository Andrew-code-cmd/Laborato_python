from tkinter import *
from tkinter.ttk import *

root = Tk()

def sec_wind():
    root_2 = Toplevel()
    global var
    var = BooleanVar()
    var.set(1)
    f_top = Frame(root_2)
    s_bot = Frame(root_2)
    r_f = Frame(root_2)
    f_f = Frame(root_2)
    l1 = Label(f_top, text='x1')
    global e1
    e1 = Entry(f_top, width=4)
    l2 = Label(f_top, text='y1')
    global e2
    e2 = Entry(f_top, width=4)
    l3 = Label(s_bot, text='x2')
    global e3
    e3 = Entry(s_bot, width=4)
    l4 = Label(s_bot, text='y2')
    global e4
    e4 = Entry(s_bot, width=4)
    r1 = Radiobutton(r_f, text="Прямоугольник", value=0, variable=var)
    r2 = Radiobutton(r_f, text="Овал", value=1, variable=var)
    b1 = Button(f_f, text="Нарисовать", command=draw)
    f_top.pack()
    s_bot.pack()
    r_f.pack()
    f_f.pack()
    l1.pack(side=LEFT)
    e1.pack(side=LEFT)
    l2.pack(side=LEFT)
    e2.pack(side=LEFT)
    l3.pack(side=LEFT)
    e3.pack(side=LEFT)
    l4.pack(side=LEFT)
    e4.pack(side=LEFT)
    r1.pack()
    r2.pack(side=LEFT)
    b1.pack(side=LEFT)

def draw():
    if var.get() == False:
        c.create_rectangle(e1.get(), e2.get(), e3.get(), e4.get())
        print("kv")
    elif var.get() == True:
        c.create_oval(e1.get(), e2.get(), e3.get(), e4.get(), width=2)
        print("oval")

c = Canvas(root, width=300, height=200, bg="white")
c.pack()

Button(text='Добавить фигуру', width=20, command=sec_wind).pack()

root.mainloop()