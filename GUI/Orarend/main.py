import tkinter as tk
from tkinter.constants import CENTER
import tkinter.font as tkFont
from napok import *

root = tk.Tk()
root.title("Órarend")
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

ft = tkFont.Font(family='Helvetica',weight="bold", size=10)

lft = tkFont.Font(family='Helvetica',weight="bold", size=24)

olabel = tk.Label(root, text="", justify=CENTER)


def gomb1_command():

    olabel["font"] = lft
    ctext="\n".join(list_hetfo)
    olabel.config(text=ctext)
    olabel.place(x=250, y=150)


def gomb2_command():

    olabel["font"] = lft
    ctext="\n".join(list_kedd)
    olabel.config(text=ctext)
    olabel.place(x=250, y=150)


def gomb3_command():

    olabel["font"] = lft
    ctext="\n".join(list_szerda)
    olabel.config(text=ctext)
    olabel.place(x=250, y=150)


def gomb4_command():

    olabel["font"] = lft
    ctext="\n".join(list_csut)
    olabel.config(text=ctext)
    olabel.place(x=250, y=150)


def gomb5_command():

    olabel["font"] = lft
    ctext="\n".join(list_pentek)
    olabel.config(text=ctext)
    olabel.place(x=250, y=150)


entry=tk.Entry(root)
entry["borderwidth"] = "1px"
entry["fg"] = "#333333"
entry["justify"] = "center"
entry["text"] = "Entry"
entry.place(x=0,y=0,width=598,height=30)

gomb1=tk.Button(root)
gomb1["bg"] = "#efefef"
gomb1["font"] = ft
gomb1["fg"] = "#000000"
gomb1["justify"] = "center"
gomb1["text"] = "Hétfő"
gomb1.place(x=0,y=50,width=120,height=30)
gomb1["command"] = gomb1_command

gomb2=tk.Button(root)
gomb2["bg"] = "#efefef"
gomb2["font"] = ft
gomb2["fg"] = "#000000"
gomb2["justify"] = "center"
gomb2["text"] = "Kedd"
gomb2.place(x=120,y=50,width=120,height=30)
gomb2["command"] = gomb2_command

gomb3=tk.Button(root)
gomb3["bg"] = "#efefef"
gomb3["font"] = ft
gomb3["fg"] = "#000000"
gomb3["justify"] = "center"
gomb3["text"] = "Szerda"
gomb3.place(x=240,y=50,width=120,height=30)
gomb3["command"] = gomb3_command

gomb4=tk.Button(root)
gomb4["bg"] = "#efefef"
gomb4["font"] = ft
gomb4["fg"] = "#000000"
gomb4["justify"] = "center"
gomb4["text"] = "Csütörtök"
gomb4.place(x=360,y=50,width=120,height=30)
gomb4["command"] = gomb4_command

gomb5=tk.Button(root)
gomb5["bg"] = "#efefef"
gomb5["font"] = ft
gomb5["fg"] = "#000000"
gomb5["justify"] = "center"
gomb5["text"] = "Péntek"
gomb5.place(x=480,y=50,width=120,height=30)
gomb5["command"] = gomb5_command

root.mainloop()
