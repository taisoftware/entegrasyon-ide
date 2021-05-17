import sys
from tkinter import filedialog
from tkinter.font import BOLD
if sys.version_info.major == 2:
    exit()
elif sys.version_info.major == 3:
    import builtins as builtins
    import tkinter as tk
import io
import tokenize
import keyword
from tkinter import *
import os
from os import read, startfile
from tkinter.filedialog import askopenfilename

root = tk.Tk()
root.geometry("1000x600")
menubar = Menu(root)
def oynat():
    dosya_uzantisi = open("dosya_uzantisi.txt","r",encoding="utf-8")
    uzanti = dosya_uzantisi.read()
    dosya_uzantisi.close()
    veri=text.get(1.0,"end-1c")
    a = open(uzanti,"w",encoding="utf-8")
    a.write(veri)
    os.startfile(r''+uzanti+'')
def runner(event):
    dosya_uzantisi = open("dosya_uzantisi.txt","r",encoding="utf-8")
    uzanti = dosya_uzantisi.read()
    dosya_uzantisi.close()
    veri=text.get(1.0,"end-1c")
    a = open(uzanti,"w",encoding="utf-8")
    a.write(veri)
    os.startfile(r''+uzanti+'')
root.config(menu=menubar)
def aç():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Python Files","*.py"),("all files","*.*")))
    dosya_uzantisi = open("dosya_uzantisi.txt","w",encoding="utf-8")
    dosya_uzantisi.write(filename)
    text.delete('1.0', END)
    p = open(filename,"r",encoding="utf-8")
    text.insert(END, p.read())
    p.close()
    root.title("Entegre | "+filename+" | Python IDLE")
    root.bind("<F5>",runner)
menubar.add_command(label="Open",command=aç)
menubar.add_command(label="Run",command=oynat)
def saver():
    veri=text.get(1.0,"end-1c")
    o = open("dosya_uzantisi.txt","r",encoding="utf-8")
    uzanti = o.read()
    ı = open(uzanti,"w",encoding="utf-8")
    ı.write(veri)
menubar.add_command(label="Save",command=saver)
def settings():
    ayarlar = Tk()
    ayarlar.iconbitmap("teko.ico")
    ayarlar.resizable(0,0)
    ayarlar.title("Entegre | Settings")
    başlık = Label(ayarlar, text="Font-Size")
    başlık.config(font=("Courier New",10,BOLD))
    başlık.place(x=0,y=0)

    def f25():
        text.config(font=("Courier New", 5,BOLD))
    def f50():
        text.config(font=("Courier New", 7,BOLD))
    def f100():
        text.config(font=("Courier New", 10,BOLD))
    def f150():
        text.config(font=("Courier New", 15,BOLD))
    uzaklık1 = Button(ayarlar, text="%25",command=f25)
    uzaklık1.place(x=0,y=20,width=50,height=20)
    uzaklık2 = Button(ayarlar, text="%50",command=f50)
    uzaklık2.place(x=50,y=20,width=50,height=20)
    uzaklık3 = Button(ayarlar, text="%100",command=f100)
    uzaklık3.place(x=100,y=20,width=50,height=20)
    uzaklık4 = Button(ayarlar, text="%150",command=f150)
    uzaklık4.place(x=150,y=20,width=50,height=20)
    ayarlar.mainloop()
menubar.add_command(label="Settings",command=settings)
root.title("Entegre | Python IDLE")
root.iconbitmap("teko.ico")

text = Text(root, fg="black", bg="white", borderwidth=0,insertbackground="black",insertwidth=2,selectforeground="black",selectbackground="#fff9d3", wrap="none")
text.pack(side="left")
text.pack(fill="both", expand=True)
text.config(font=("Courier New",10))

y_scrollbar = Scrollbar(text, cursor="arrow")
y_scrollbar.pack(side="right", fill="y")
y_scrollbar["orient"] = "vertical"
y_scrollbar["command"] = text.yview

x_scrollbar = Scrollbar(text, cursor="arrow")
x_scrollbar.pack(side="bottom", fill="x")
x_scrollbar["orient"] = "horizontal"
x_scrollbar["command"] = text.xview

text["yscrollcommand"] = y_scrollbar.set
text["xscrollcommand"] = x_scrollbar.set

count = 0

def colorize(*args):
    global count
    row1, col1 = args[0].start
    row1, col1 = str(row1), str(col1)
    row2, col2 = args[0].end
    row2, col2 = str(row2), str(col2)
    start = ".".join((row1, col1))
    end = ".".join((row2, col2))
    text.tag_add(str(count), start, end)
    try:
        text.tag_config(str(count), foreground=args[1], font=args[2])
    except IndexError:
        text.tag_config(str(count), foreground=args[1])
    count += 1

def search(event):
    try:
        for i in tokenize.tokenize(io.BytesIO(text.get("1.0", "end").encode("utf-8")).readline):
            if i.type == 1:
                if i.string in keyword.kwlist:
                    colorize(i, "tomato")
                elif i.string in dir(builtins):
                    colorize(i, "#423189")
                else:
                    colorize(i, "black")
            elif i.type == 2:
                colorize(i, "#90EE90")
            elif i.type == 3:
                colorize(i, "#3abc2a")
            elif i.type == 53:
                if i.string == "," or i.string == "." or i.string == ":":
                    colorize(i, "orange")
                elif i.string == "(" or i.string == ")" or i.string == "[" \
                        or i.string == "]" or i.string == "{" or i.string == "}":
                    colorize(i, "orange")
                else:
                    colorize(i, "green")
            elif i.type == 57:
                colorize(i, "grey", "TkDefaultFont 10 italic")
    except tokenize.TokenError:
        pass

def ex(event):
    exit()
root.bind("<Control-w>",ex)
text.bind("<KeyRelease>", search)

root.mainloop()
