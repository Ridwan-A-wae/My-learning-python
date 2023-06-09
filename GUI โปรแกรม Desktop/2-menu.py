from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("My GUI")
root.geometry("500x300")

# สร้างเมนู
myMenu = Menu()
root.config(menu=myMenu)

# สร้างหน้าต่างใหม่
def openNew():
    newWindow= Tk()
    newWindow.title('New Window')
    newWindow.geometry("200x200")
    newWindow.mainloop()

def aboutProgram():
    tkinter.messagebox.showinfo("รายละเอียดโปรแกรม","ผู้พัฒนาโปรแกรมคือClaims")

def exitProgram():
    confirm = tkinter.messagebox.askquestion("แจ้งเตือน","คุณต้องการปิดโปรแกรมหรือไม่")
    if(confirm =="yes"):
            root.destroy()


# สร้าง เมนูย่อย (Menu item)
menuItem = Menu()
menuItem.add_command(label="New Window",command=openNew)
menuItem.add_command(label="Open")
menuItem.add_command(label="Save")
menuItem.add_command(label="About",command=aboutProgram)
menuItem.add_command(label="Exit",command=exitProgram)

# เพิ่มเมนูต่อไปเช่นเดียวกัน
myMenu.add_cascade(label="File",menu=menuItem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")



root.mainloop()