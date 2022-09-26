from tkinter import *
from tkinter.ttk import *
root = Tk()

def sec_wind():
    root_2 = Toplevel()
    global var
    var = IntVar()
    var.set(1)
    Label(root_2, text="x1").grid(row=0, column=0)
    global e1
    e1 = Entry(root_2, width=4)
    e1.grid(row=0, column=1, columnspan=2)
    Label(root_2, text="y1").grid(row=0, column=3)
    global e2
    e2 = Entry(root_2, width=4)
    e2.grid(row=0, column=4, columnspan=2)
    Label(root_2, text="x2").grid(row=1, column=0)
    global e3
    e3 = Entry(root_2, width=4)
    e3.grid(row=1, column=1, columnspan=2)
    Label(root_2, text="y2").grid(row=1, column=3)
    global e4
    e4 = Entry(root_2, width=4)
    e4.grid(row=1, column=4, columnspan=2)
    r1 = Radiobutton(root_2, text="Прямоугольник", value=0, variable=var)
    r1.grid(row=2, column=0, columnspan=5)
    r2 = Radiobutton(root_2, text="Овал", value=1, variable=var)
    r2.grid(row=3, column=0, columnspan=3)
    b1 = Button(root_2, text="Нарисовать", command=draw)
    b1.grid(row=4, column=0, columnspan=4)
    
def draw():
    try:
        if var.get() == 0:
            c.create_rectangle(e1.get(), e2.get(), e3.get(), e4.get())
            print("kv")
        elif var.get() == 1:
            c.create_oval(e1.get(), e2.get(), e3.get(), e4.get(), width=2)
            print("oval")
    except:

        print('some error was come')
c = Canvas(root, width=300, height=200, bg="white")
c.pack()

Button(text='Добавить фигуру', width=20, command=sec_wind).pack()


root.mainloop()