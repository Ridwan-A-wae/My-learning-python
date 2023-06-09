# ชื่อ , เงินเดือน

# สร้าง class
class Employee:

    # สร้าง method
    def detail(self,empName,empSalary,empDepartment):
        self.name = empName
        self.salary = empSalary
        self.department = empDepartment

    def showData(self):
            print("Name  = {}".format(self.name))
            print("Salary = {} THB".format(self.salary))
            print("Department = {}".format(self.department))


# การสร้าง object
obj1 = Employee()
obj1.detail("Genji",30000,"DPS")

obj2 = Employee()
obj2.detail("Winston",25000,"Tank")

obj3 = Employee()
obj3.detail("Hanzo",50000,"DPS")

obj1.showData()
obj2.showData()
obj3.showData()