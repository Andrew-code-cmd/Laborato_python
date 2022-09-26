from calendar import c
from tkinter import *
from turtle import bgcolor, color

root = Tk()
cx = 0
cy = 90
cs = 20
ce = 200

c = Canvas(root, bg='white', width=240, height=150)
c.pack(fill=BOTH, expand=1)
box = c.create_rectangle(40, 40, 100, 100, fill='lightblue')
roof = c.create_polygon(30,40, 110, 40, 70, 10, fill = 'lightblue', outline = 'black')
sun = c.create_oval(130, 14, 155, 40, width=0, fill='orange')
for i in range (5, 200, 10):
    c.create_arc(cx + i, cy, cs + i, ce, 
             start=160, extent=-90, 
             style=ARC, outline='green', 
             width=2)

root.mainloop()