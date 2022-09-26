
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd

def insertText():
    try:
        file_name = fd.askopenfilename()
        f = open(file_name)
        s = f.read()
        text.insert(1.0, s)
        f.close()
    except:
        mb.showerror(title='error', message='файл не загружен')

def extractText():
    try:
        file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"), ("HTML files", "*.html"),
        ("All files", "*.*")))
        f = open(file_name, 'w')
        s = text.get(1.0, END)
        f.write(s)
        f.close()
    except:
        mb.showerror(title='error', message='файл не сохранен')

def clear_field():
    ans = mb.askyesno(message="Вы действительно хотите удалить содержимое файла?", title="IMPORTANT")
    if ans == True:
        text.delete("1.0","end")

root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insertText)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extractText)
b2.grid(row=1, column=1, sticky=W)
b3 = Button(text="Очистить", command=clear_field)
b3.grid(row=1, column=1)
root.mainloop()