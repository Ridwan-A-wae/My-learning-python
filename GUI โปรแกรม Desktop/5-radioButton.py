from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("My GUI")
root.geometry("500x300")


language = IntVar()
language.set(2)

def showChoice():
    choice = language.get()
    if choice == 1:
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณได้เลือกตัว Python")
    elif choice == 2:
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณได้เลือกตัว Javascipt")
    elif choice == 3:
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณได้เลือกตัว PHP")
    else :
        tkinter.messagebox.showinfo("แจ้งเตือน","คุณได้เลือกตัว C#")

#เลือกได้แค่ 1 ตัว โดยกำหนดให้ทั้ง 4 อยู๋ในตัวแปรเดียวกัน
Radiobutton(text="Python",variable=language,value=1,command=showChoice).grid(row=0,column=0)
Radiobutton(text="Jasvacipt",variable=language,value=2,command=showChoice).grid(row=0,column=1)
Radiobutton(text="PHP",variable=language,value=3,command=showChoice).grid(row=0,column=2)
Radiobutton(text="C#",variable=language,value=4,command=showChoice).grid(row=0,column=3)




root.mainloop()