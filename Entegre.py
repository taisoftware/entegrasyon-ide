from tkinter import filedialog
from tkinter import *
root = Tk()
root.geometry("1000x600")
menubar = Menu(root, background="#191919", fg="tomato")
def aç():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
    if filename != "":
        dosya_uzantisi = open("file_path.txt","w",encoding="utf-8")
        dosya_uzantisi.write(filename)
        dosya_uzantisi.close()
        text.config(state="normal")
        text.delete('1.0', END)
        p = open(filename,"r",encoding="utf-8")
        text.insert(END, p.read())
        p.close()
        menubar.entryconfig("Save", state="active")
        root.title("Entegre ["+filename+"]")
        def değiştir(event):
            if "*" not in root.title():
                root.title("*"+root.title())
        text.bind("<Key>", değiştir)
        def savere(event):
            titl = root.title()
            titl = titl.replace("*","")
            root.title(titl)
            veri=text.get(1.0,"end-1c")
            o = open("file_path.txt","r",encoding="utf-8")
            uzanti = o.read()
            o.close()
            ı = open(uzanti,"w",encoding="utf-8")
            ı.write(veri)
            ı.close()
        root.bind("<Control-s>",savere)
menubar.add_command(label="Open",command=aç)
def saver():
    titl = root.title()
    titl = titl.replace("*","")
    root.title(titl)
    veri=text.get(1.0,"end-1c")
    o = open("file_path.txt","r",encoding="utf-8")
    uzanti = o.read()
    o.close()
    ı = open(uzanti,"w",encoding="utf-8")
    ı.write(veri)
    ı.close()
menubar.add_command(label="Save",command=saver)
menubar.entryconfig("Save", state="disabled")
filemenu = Menu(menubar, tearoff=0)
root.config(menu=menubar)
root.title("Entegre [...]")
root.iconbitmap("icon.ico")
text = Text(root, fg="black", bg="white", borderwidth=0, undo=True,insertbackground="black",insertwidth=2,selectforeground="black",selectbackground="orange", wrap="none")
text.pack(side="left")
text.pack(fill="both", expand=True)
text.config(font=("Courier New",10),state="disable")
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
def ex(event):
    exit()
root.bind("<Control-w>",ex)
root.mainloop()
