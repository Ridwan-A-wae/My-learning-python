class Employee:

    # class variable 
    minSalary = 12000
    maxSalary = 70000
    companyName = "XYZ co"

    # constuctor
    def __init__(self,empName,empSalary,empDepartment):
        self.__name = empName
        self._salary = empSalary
        self.__department = empDepartment

    # method
    def _showData(self):
        print("Name  = {}".format(self.__name))
        print("Salary = {} THB".format(self._salary))
        print("Department = {}".format(self.__department))

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self):
        pass
class Programer(Employee):
    __departmentName = "แผนกพัฒนา"
    def __init__(self):
        pass
class Sale(Employee):
    __departmentName = "ฝ่ายขาย"
    def __init__(self):
        pass


account = Accounting()
programer = Programer()
sale = Sale()
