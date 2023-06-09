# 1 บาทไทย = 0.026 EUR ยูโร
# 1 บาทไทย = 3.486 JPY เยน
# 1 บาทไทย = 0.031 USD ดอลล่า
# 1 บาทไทย = 0.023 GBP ปอนด์


from tkinter import *
from tkinter import ttk

root = Tk()
root.title("โปรแกรมแปลงสกุลเงิน")


# input
money = IntVar()
Label(text="จำนวนเงิน(THB)",padx=10,font=30).grid(row=0,sticky=W)
et1 = Entry(font=30,width=30,textvariable=money)
et1.grid(row=0,column=1)

choice = StringVar(value="โปรดเลือกจำนวณเงิน")
Label(text="เลือกสกุลเงิน",padx=10,font=30).grid(row=1,sticky=W)
combo = ttk.Combobox(width=30,font=30,textvariable=choice)
combo.grid(row=1,column=1)
combo["values"] = ("EUR","JPY","USD","GBP")


#output
Label(text="ผลการคำนวณ",padx=10,font=30).grid(row=2,sticky=W)
et2 = Entry(font=30,width=30,)
et2.grid(row=2,column=1)

def calculate():
    amount = money.get()
    currency = choice.get()
    if currency == "EUR":
        et2.delete(0,END)
        result = ((amount*0.026),"EUR")
        et2.insert(0,result)
    elif currency =="JPY":
        et2.delete(0,END)
        result = ((amount*3.486),"JPY")
        et2.insert(0,result)
    elif currency =="USD":
        et2.delete(0,END)
        result = ((amount*0.031),"USD")
        et2.insert(0,result)
    elif currency =="GBP":
        et2.delete(0,END)
        result = ((amount*0.023),"GBP")
        et2.insert(0,result)
    else :
        pass

def clear():
    et1.delete(0,END)
    et2.delete(0,END)
    combo.delete(0,END)

Button(text="คำนวณ",font=30,width=15,command=calculate).grid(row=3,column=1,sticky=W)
Button(text="ล้างค่า",font=30,width=15,command=clear).grid(row=3,column=1,sticky=E)

root.mainloop()