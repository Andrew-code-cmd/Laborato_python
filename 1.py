from tkinter import *

root = Tk()

e1 = Entry(width=20, justify=CENTER)
e2 = Entry(width=20, justify=CENTER)
l = Label(text='', justify=CENTER)

def plus():
    try:
         l['text'] = int(e1.get()) + int(e2.get())
    except:
        l['text'] = 'error'
def minus():
    try:
         l['text'] = int(e1.get()) - int(e2.get())
    except:
        l['text'] = 'error'
def mul():
    try:
         l['text'] = int(e1.get()) * int(e2.get())
    except:
        l['text'] = 'error'
def div():
    try:
         l['text'] = int(e1.get()) / int(e2.get())
    except:
        l['text'] = 'error'

e1.pack()
e2.pack()
l.pack()

plus = Button(width=3, text="+", command=plus).pack(side=LEFT)
minus = Button(width=3, text="-", command=minus).pack(side=LEFT)
mul = Button(width=3, text="*", command=mul).pack(side=LEFT)
div = Button(width=3, text="/", command=div).pack(side=LEFT)

root.mainloop()