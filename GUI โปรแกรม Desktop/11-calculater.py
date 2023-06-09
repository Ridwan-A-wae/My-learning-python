from tkinter import *
root = Tk()
root.title("เครื่องคิดเลข")


content = ""
txt_imput = StringVar(value="0",)

def btn(number):
    global content
    content = content+str(number)
    txt_imput.set(content)

def equal():
    global content
    calculate = float(eval(content))
    txt_imput.set(calculate)
    calculate = ""

def clear():
    global content
    content = ""
    txt_imput.set("")
    display.insert(0,"0")


# แสดงผล
display = Entry(font=("arial",30,'bold'),textvariable=txt_imput,fg="white",bg="green",justify="right")
display.grid(columnspan=4)

#รับค่าผ่านปุ่ม
btn7 = Button(text="7",command=lambda:btn(7),fg="black",font=("arial",30,'bold'),padx=30,pady=15).grid(row=1,column=0)
btn8 = Button(text="8",command=lambda:btn(8),fg="black",font=("arial",30,'bold'),padx=30,pady=15).grid(row=1,column=1)
btn9 = Button(text="9",command=lambda:btn(9),fg="black",font=("arial",30,'bold'),padx=30,pady=15).grid(row=1,column=2)
btnClear = Button(text="C",command=clear,fg="black",font=("arial",30,'bold'),padx=30,pady=15).grid(row=1,column=3)

btn4 = Button(text="4",command=lambda:btn(4),fg="black",font=("arial",30,'bold'),padx=30,pady=15).grid(row=2,column=0)
btn5 = Button(text="5",command=lambda:btn(5),fg="black",font=("arial",30,'bold'),padx=30,pady=15).grid(row=2,column=1)
btn6 = Button(text="6",command=lambda:btn(6),fg="black",font=("arial",30,'bold'),padx=30,pady=15).grid(row=2,column=2)
btnPlus = Button(text="+",command=lambda:btn("+"),bg="orange",fg="black",font=("arial",30,'bold'),padx=35,pady=15).grid(row=2,column=3)

btn1 = Button(text="1",command=lambda:btn(1),fg="black",font=("arial",30,'bold'),padx=30,pady=15).grid(row=3,column=0)
btn2 = Button(text="2",command=lambda:btn(2),fg="black",font=("arial",30,'bold'),padx=30,pady=15).grid(row=3,column=1)
btn3 = Button(text="3",command=lambda:btn(3),fg="black",font=("arial",30,'bold'),padx=30,pady=15).grid(row=3,column=2)
btnMinus = Button(text="-",command=lambda:btn("-"),bg="orange",fg="black",font=("arial",30,'bold'),padx=40,pady=15).grid(row=3,column=3)

btn0 = Button(text=".",command=lambda:btn("."),fg="black",font=("arial",30,'bold'),padx=30,pady=15).grid(row=4,column=0)
btnDot = Button(text="0",command=lambda:btn(0),fg="black",font=("arial",30,'bold'),padx=30,pady=15).grid(row=4,column=1)
btnDivision = Button(text="/",command=lambda:btn("/"),bg="orange",fg="black",font=("arial",30,'bold'),padx=35,pady=15).grid(row=4,column=2)
btnMultiply = Button(text="x",command=lambda:btn("*"),bg="orange",fg="black",font=("arial",30,'bold'),padx=35,pady=15).grid(row=4,column=3)

btneqoul = Button(text="=",command=equal,fg="black",bg="cyan",font=("arial",30,'bold'),padx=95,pady=15,).grid(row=5,column=0,columnspan=2)
btnopen = Button(text="(",command=lambda:btn("("),fg="black",bg="orange",font=("arial",30,'bold'),padx=35,pady=15).grid(row=5,column=2)
btnclose = Button(text=")",command=lambda:btn(")"),fg="black",bg="orange",font=("arial",30,'bold'),padx=35,pady=15).grid(row=5,column=3)

root.mainloop()