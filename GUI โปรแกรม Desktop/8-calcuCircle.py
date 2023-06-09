from tkinter import *
root = Tk()
root.title("คำนวณพื้นที่วงกลม")
root.geometry("200x200")

# พื้นที่วงกลม = พาย อา 2 โดยให้ค่า พาย มีค่า 3.14

Label(text="รัศมี",font=30).grid(row=0,column=0)
etVar1 = IntVar()
et1 = Entry(textvariable=etVar1)
et1.grid(row=0,column=1)

Label(text="พื้นที่วงกลม",font=30).grid(row=1,column=0)
et2 = Entry()
et2.grid(row=1,column=1)


def calculante():
    e = etVar1.get()
    area = 3.14 *e*e
    et2.insert(0,area)

def clear():
    et1.delete(0,END)
    et2.delete(0,END)

btn = Button(text="คำนวณ",command=calculante).grid(row=3,column=0)
btn = Button(text="ล้างค่า",command=clear).grid(row=4,sticky=E)


root.mainloop()