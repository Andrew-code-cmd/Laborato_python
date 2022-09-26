from tkinter import *

root = Tk()
    
l = Label(text="", justify=CENTER)
el = Entry(width=22, justify=CENTER)

#обработчики нажатия
def red_click():
    el.delete(0, END)
    el.insert(0, "ff7d00")
    l['text'] = 'красный'
def o_click():
    el.delete(0, END)
    el.insert(0, "#ff7d00")
    l['text'] = "оранжевый"
def y_click():
    el.delete(0, END)
    el.insert(0, "#ffff00")
    l['text'] = "желтый"
def g_click():
    el.delete(0, END)
    el.insert(0, "#00ff00")
    l['text'] = "зеленый"
def f_click():
    el.delete(0, END)
    el.insert(0, "#007dff")
    l['text'] = "голубой"
def s_click():
    el.delete(0, END)
    el.insert(0, "#0000ff")
    l['text'] = "синий"
def p_click():
    el.delete(0, END)
    el.insert(0, "#7d00ff")
    l['text'] = "фиолетовый"

l.pack()
el.pack()

#да, я пытался сделать через словарь. Но позорно обосрался
red = Button(width=2, bg="#ff0000", command=red_click).pack(side=LEFT)
orange = Button(width=2, bg="#ff7d00", command=o_click).pack(side=LEFT)
yellow = Button(width=2, bg="#ffff00", command=y_click).pack(side=LEFT)
green = Button(width=2, bg="#00ff00", command=g_click).pack(side=LEFT)
f_blue = Button(width=2, bg="#007dff", command=f_click).pack(side=LEFT)
s_blue = Button(width=2, bg="#0000ff", command=s_click).pack(side=LEFT)
purple = Button(width=2, bg="#7d00ff", command=p_click).pack(side=LEFT)

root.mainloop()
