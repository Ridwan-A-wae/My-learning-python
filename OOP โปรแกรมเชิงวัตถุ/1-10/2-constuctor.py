# ชื่อ , เงินเดือน

# สร้าง class
class Employee:
    ## ต่าเริ่มต้นของ Constuctor 
    #Default Constuctor
    def __init__(self,empName,empSalary,empDepartment):
        self.name = empName
        self.salary = empSalary
        self.department = empDepartment

    def showData(self):
            print("Name  = {}".format(self.name))
            print("Salary = {} THB".format(self.salary))
            print("Department = {}".format(self.department))


# การสร้าง object
obj1 = Employee("Genji",30000,"DPS")
obj1.salary = 60000
obj2 = Employee("Winston",25000,"Tank")
obj2.department = "DPS"
obj3 = Employee("Hanzo",50000,"DPS")
obj3.name = "Ana"
obj3.salary = 70000
obj3.department="Heal"


obj1.showData()
obj2.showData()
obj3.showData()