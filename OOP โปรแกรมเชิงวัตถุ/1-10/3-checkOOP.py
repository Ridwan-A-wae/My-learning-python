class Employee:

    def __init__(self,empName,empSalary,empDepartment):
        self.name = empName
        self.salary = empSalary
        self.department = empDepartment

    def showData(self):
            print("Name  = {}".format(self.name))
            print("Salary = {} THB".format(self.salary))
            print("Department = {}".format(self.department))



obj1 = Employee("Genji",30000,"DPS")
obj2 = Employee("Winston",25000,"Tank")
obj3 = Employee("Hanzo",50000,"DPS")

# isinstance เช็คว่า obj1 ถูกสร้างมาจาก class Employee หรือเปล่า
print(isinstance(obj1,Employee))

# dir เช็คว่า obj2 มี attribute , method อะไรบ้าง
print( dir(obj2))

# __class__ เช็คว่า obj3 ถูกสร้างมาจาก class ไหน
print(obj3.__class__)