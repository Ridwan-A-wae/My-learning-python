class Employee:

    # class variable 
    minSalary = 12000
    maxSalary = 70000
    companyName = "XYZ co"

    # constuctor
    def __init__(self,empname,empsalary,empDepartment):
        #instance variable
        self.__name = empname
        self.__salary = empsalary
        self.__department = empDepartment

    # method
    def _showData(self):
        print("Name  = {}".format(self.__name))
        print("Salary = {} THB".format(self.__salary))
        print("Department = {}".format(self.__department))

class Accounting(Employee):
    __departmentName = "Accounting"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
class Programer(Employee):
    __departmentName = "Programer"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
class Sale(Employee):
    __departmentName = "Sale"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)


account = Accounting("genji",30000)
programer = Programer("Hanzo",35000)
sale = Sale("Ana",40000)

account._showData()
programer._showData()
sale._showData()
