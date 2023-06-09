class Employee:

    # class variable สามารถเรียกใช้ได้ทันที ผ่าน Employee
    _minSalary = 12000
    _maxSalary = 70000


    def __init__(self,empName,empSalary,empDepartment):
        #instance variable ต้องใช้ object ในการเรีกยใช้
        self.__name = empName
        self._salary = empSalary
        self.__department = empDepartment

        #private method
    def _showData(self):
        print("Name  = {}".format(self.__name))
        print("Salary = {} THB".format(self._salary))
        print("Department = {}".format(self.__department))

    # setter method
    def setName(self,newname):
        self.__name = newname

# instance variable
obj1 = Employee("Genji",30000,"DPS")
obj1._showData()

# class variable
print(Employee._minSalary)

