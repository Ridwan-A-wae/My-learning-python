from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

def selectColor():
    color = askcolor()
    myLabel = Label(text='Hello python',bg=color[1]).pack()

def selectFile():
    fileOpen = askopenfilename()
    readFile = open(fileOpen,encoding="utf8")
    myLabel = Label(text=readFile.read()).pack()

btn = Button(text='เลือกสี',command=selectColor).pack()
btn = Button(text='เลือกไฟล์',command=selectFile).pack()

root.mainloop()