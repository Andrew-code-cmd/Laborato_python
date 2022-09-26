from tkinter import *

root = Tk()

text = Text(width=40, height=20, wrap=WORD)
text.pack(expand=True, fill=BOTH, side=BOTTOM)
e = Entry(width=20)
arr_b_open=[]
arr_b_save=[]
arr_text=[]
def b_open():
    #Если блок try выполняется, в массив добавляется 1(для unittest)
    try:
        with open(f'C:/Users/user/Desktop/лабораторные/{e.get()}', 'r+') as f:
            try:
                text.insert(1.0, *f)
                arr_text.append(1)
            except:
                pass
        arr_b_open.append(1)
    except:
        pass
def b_save():
    try:
        with open(f'C:/Users/user/Desktop/лабораторные/{e.get()}', 'w') as f:
            f.write(text.get(1.0, END))
        arr_b_save.append(1)
    except:
        pass

e.pack(side=LEFT)

b1 = Button(width=14, text='Открыть', command=b_open).pack(side=LEFT)
b2 = Button(width=14, text='Сохранить', command=b_save).pack(side=LEFT)
root.mainloop()

