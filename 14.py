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

mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...", command=insertText)
filemenu.add_command(label="Сохранить", command=extractText)

textmenu = Menu(mainmenu, tearoff=0)
textmenu.add_command(label='Очистить', command=clear_field)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Поле", menu=textmenu)

text = Text(width=50, height=25)
text.grid(columnspan=2)

root.mainloop()