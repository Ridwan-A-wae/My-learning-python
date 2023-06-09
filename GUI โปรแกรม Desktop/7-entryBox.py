from tkinter import *
root = Tk()
root.title("Data Entry")
root.geometry("200x200")


Label(text="ชื่อ").grid(row=0)
Label(text="นามสกุล").grid(row=1)
Label(text="เบอร์โทร").grid(row=2)



et1 = Entry()
et1.grid(row=0,column=1)
et1.insert(0,"Cim")
et2 = Entry()
et2.grid(row=1,column=1)
et2.insert(0,"Las")
et3 = Entry()
et3.grid(row=2,column=1)
et3.insert(0,"0611546545")

def clearText():
    et1.delete(0,END)
    et2.delete(0,END)
    et3.delete(0,END)

Button(text="ล้างข้อมูล",command=clearText).grid(row=3,column=1)

root.mainloop()