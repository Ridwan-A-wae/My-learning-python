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
        print("Name  = "+self.__name)
        print("Salary = {} THB".format(self.__salary))
        print("Department = "+self.__department)

        #รายได้ต่อปี
    def _getincome(self,bonus=0):
        return (self.__salary * 12)+bonus
    
        #Object แปลงเป็น String   ทำให้มันเป็นชุดข้อความไปเลย
    def __str__(self):
        return ("Name is {}, Salary = {}THB, from {}, Salary per year = {}THB".format(self.__name,self.__salary,self.__department,self._getincome()))
    