from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

def selectColor():
    color = askcolor()
    myLabel = Label(text='Hello python',bg=color[1]).pack()

btn = Button(text='เลือกสี',command=selectColor).pack()

root.mainloop()