from tkinter import *

def change(event):
    try:
        text.configure(width=e1.get(), height=e2.get())
    except:
        print("что-то не так")
        
#НЕ ЗАБУДЬТЕ ПРО CTRL+TAB
def e(event):
    try:
        text.configure(width=e1.get(), height=e2.get())
    except:
        print("что-то не так")

def focus(event):
    if text.focus_get():
        text.configure(bg='white')

def focus_out(event):
    if text.focus_get() != '.!text':
        text.configure(bg='lightgrey')

root = Tk()

text = Text(width=25, height=12, bg='lightgrey')
text.bind('<FocusIn>', focus)
text.bind('<FocusOut>', focus_out)
text.pack(side=BOTTOM)
b_edit = Button(text='Изменить')
b_edit.bind('<Button-1>', change)
b_edit.bind('<Return>', e)

b_edit.pack(side=RIGHT)
e1 = Entry(width=5)
e1.pack()
e2 = Entry(width=5)
e2.pack()


root.mainloop()