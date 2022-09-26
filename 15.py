from tkinter import *
from random import randint

def click():
    b.place(x=randint(1, 100), y=randint(1, 100))

root = Tk()

root.geometry('300x300')
img = PhotoImage(file='C:/Users/user/Desktop/лабораторные/1.png')
b = Button(image=img, width=50, height=50, command=click)
b.pack()



root.mainloop()