from tkinter import *


root = Tk()

lbox = Listbox(selectmode=MULTIPLE)
lbox2 = Listbox(selectmode=MULTIPLE)

def add():
    select1 = lbox.curselection()
    for i in select1[::-1]:
        selected = lbox.get(i)
        lbox2.insert(0, selected)
    
def delete():
    selected = lbox2.curselection()
    for selected in selected[::-1]:
        lbox2.delete(selected)

lbox.pack(side=LEFT)
lbox2.pack(side=RIGHT)

l = Label(text="", height=3).pack()
b1 = Button(width=8, text=">>>", command=add).pack()
b2 = Button(width=8, text="<<<", command=delete).pack()


for i in ('apple', 'bananas', 'carrot', 'bread'):
    lbox.insert(0, i)


root.mainloop()