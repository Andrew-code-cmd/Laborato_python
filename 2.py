from tkinter import *

root = Tk()
    
l = Label(text="", justify=CENTER)
el = Entry(width=22, justify=CENTER)

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
red = Button(width=18, bg="#ff0000", command=red_click).pack()
orange = Button(width=18, bg="#ff7d00", command=o_click).pack()
yellow = Button(width=18, bg="#ffff00", command=y_click).pack()
green = Button(width=18, bg="#00ff00", command=g_click).pack()
f_blue = Button(width=18, bg="#007dff", command=f_click).pack()
s_blue = Button(width=18, bg="#0000ff", command=s_click).pack()
purple = Button(width=18, bg="#7d00ff", command=p_click).pack()

root.mainloop()
