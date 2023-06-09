from tkinter import *

# จอที่ 1
root = Tk()
root.title("My GUI")
# กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("500x500")




# ใส่ข้อความในหน้าจอ
myLable1 = Label(root,text="Hello World",fg="black",bg="red",font=20).pack()

def showMessage():
    message = txt.get()
    Label(root,text=message,fg="black",bg="red",font=20).pack()
# กล่องข้อความ
txt = StringVar()
myText = Entry(root,textvariable=txt).pack()

def openWindow():
    # จอที่ 2
    myWindow = Tk()
    myWindow.title("รายงานผลการทำงาน")
    myWindow.geometry("500x300")

# ใส่ปุ่ม
btn1 = Button(root,text="บันทึก",fg="white",bg="green",command=showMessage).pack()
btn2 = Button(root,text="เปิดรายงาน",fg="white",bg="red",command=openWindow).pack()






root.mainloop() 

