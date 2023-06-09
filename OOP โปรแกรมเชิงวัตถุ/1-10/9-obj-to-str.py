# class แม่
class Employee:

    # class variable 
    minSalary = 12000
    maxSalary = 70000
    companyName = "XYZ co"

    # constuctor
    def __init__(self,empname,empsalary,empDepartment):
        self.__name = empname
        self.__salary = empsalary
        self.__department = empDepartment

    # method
        #แสดงรายละเอียด
    def _showData(self):
        print("Name  = {}".format(self.__name))
        print("Salary = {} THB".format(self.__salary))
        print("Department = {}".format(self.__department))

        #รายได้ต่อปี
    def _getincome(self):
        return self.__salary * 12
    
        #Object แปลงเป็น String   ทำให้มันเป็นชุดข้อความไปเลย
    def __str__(self):
        return ("Name is {}, Salary = {}THB, from {}, Salary per year = {}THB".format(self.__name,self.__salary,self.__department,self._getincome()))
    


# class ลูก 
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

print(account.__str__())
print(programer.__str__())
print(sale.__str__())

# account._showData()
# programer._showData()
# sale._showData()
