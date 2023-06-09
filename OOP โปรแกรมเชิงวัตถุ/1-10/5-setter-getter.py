class Employee:

    def __init__(self,empName,empSalary,empDepartment):
        #private attribute
        self.__name = empName
        self.__salary = empSalary
        self.__department = empDepartment

        #private method
    def _showData(self):
        print("Name  = {}".format(self.__name))
        print("Salary = {} THB".format(self.__salary))
        print("Department = {}".format(self.__department))

    # setter method
    def setName(self,newname):
        self.__name = newname

    def setSalary(self,newsalary):
        self.__salary = newsalary
    
    def setDepartment(self,newdepartment):
        self.__department = newdepartment

    # getter method
    def getName(self):
        return self.__name
    
    def getSalary(self):
        return self.__salary
    
    def getDepartment(self):
        return self.__department

obj1 = Employee("Genji",30000,"DPS")

## การใช้ setter method
# obj1.setName("Ana")
# obj1.setSalary(60000)
# obj1.setDepartment("Support")
# obj1._showData()

## การใช้ getter method
# print(obj1.getName())
# print(obj1.getSalary())
# print(obj1.getDepartment())

## ใช้ getter แต่งโปรโยค
# print("The best Employee is",format(obj1.getName()))
# print("at = ",format(obj1.getDepartment()))
# print("salary is",format(obj1.getSalary()))