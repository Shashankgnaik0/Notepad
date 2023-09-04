import os
import win32gui,win32con
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename

#######################################

def newfile():
    global file
    root.title("Untitled-Note")
    file = None
    TextArea.delete(1.0,END)

def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file))
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())

def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file))  
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
def contact():
    showinfo("Contact",'your information here')            
def quitUI():
    quit()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Notepad made using Tkinter in Python \n made by Shashank G Naik")

###############################
root=Tk()
root.geometry("800x700")
root.title("Notepad with Tkinter")
root.wm_iconbitmap("main.ico")
#typing area
TextArea=Text(root,font= "Cursive 12")
file=None
TextArea.pack(expand=True,fill=BOTH)
#menubar starts
Menubar= Menu(root)
    #File Menu 
Filemenu= Menu(Menubar,tearoff=0,background='violet')
Filemenu.add_command(label="New",command=newfile)
Filemenu.add_command(label="Open",command=openfile)
Filemenu.add_command(label="Save",command=savefile)
Filemenu.add_separator()
Filemenu.add_command(label="Exit",command=quitUI)
Menubar.add_cascade(label="File", menu=Filemenu)
    #Edit menu
Editmenu=Menu(Menubar,tearoff=0,background='violet')
Editmenu.add_command(label="Cut",command=cut)
Editmenu.add_command(label="Copy",command=copy)
Editmenu.add_command(label="Paste",command=paste)
Menubar.add_cascade(label="Edit", menu=Editmenu)
    #Help Menu
Helpmenu=Menu(Menubar,tearoff=0,background='violet')
Helpmenu.add_command(label="About",command=about)
Helpmenu.add_command(label="Contact",command=contact)
Menubar.add_cascade(label="Help", menu=Helpmenu)
root.config(menu=Menubar)
#menu bar ends scrollbar starts
Scroll=Scrollbar(TextArea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)
#########################################