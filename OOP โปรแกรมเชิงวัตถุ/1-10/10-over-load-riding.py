#Overloading
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
    
#Overriding คือการเอา method จาก class แม่มาวางไว้ใน class ลูก แล้วปรับแต่งตาม class ลูก

# class ลูก 
class Accounting(Employee):
    __departmentName = "Accounting"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentName)
        self._age = age
        
    def _showData(self):
            super()._showData()
            print("age = "+str((self._age)))
            print("#########")


class Programer(Employee):
    __departmentName = "Programer"
    def __init__(self,name,salary,exp,skill):
        super().__init__(name,salary,self.__departmentName)
        self._exp = exp
        self._skill = skill
        
    def _showData(self):
            super()._showData()
            print("Experience = "+str(self._exp))
            print("Skill = "+str(self._skill))
            print("#########")

class Sale(Employee):
    __departmentName = "Sale"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentName)
        self._area = area

    def _showData(self):
            super()._showData()
            print("Area = "+(self._area))
            print("#########")


account = Accounting("genji",30000,23)
programer = Programer("Hanzo",35000,0,"MERN Stack")
sale = Sale("Ana",40000,"Bangkok")


# account._showData()
# programer._showData()
# sale._showData()

print("account Salary and bonus per/year ="+str(account._getincome(10000)))
print("programer Salary and bonus per/year ="+str(programer._getincome()))
print("sale Salary and bonus per/year ="+str(sale._getincome(20000)))


