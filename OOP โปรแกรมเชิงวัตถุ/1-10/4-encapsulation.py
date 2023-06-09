class Employee:


# # public
#     def __init__(self,empName,empSalary,empDepartment):
#         #public attribute
#         self.name = empName
#         self.salary = empSalary
#         self.department = empDepartment

#         #public method
#     def showData(self):
#             print("Name  = {}".format(self.name))
#             print("Salary = {} THB".format(self.salary))
#             print("Department = {}".format(self.department))
# obj1 = Employee("Genji",30000,"DPS")
# obj1.showData()


# # protected
#     def __init__(self,empName,empSalary,empDepartment):
#         #protected attribute
#         self._name = empName
#         self._salary = empSalary
#         self._department = empDepartment

#         #protected method
#     def _showData(self):
#         print("Name  = {}".format(self._name))
#         print("Salary = {} THB".format(self._salary))
#         print("Department = {}".format(self._department))

# obj1 = Employee("Genji",30000,"DPS")
# obj1._showData()



# # #private
    def __init__(self,empName,empSalary,empDepartment):
        #private attribute
        self.__name = empName
        self.__salary = empSalary
        self.__department = empDepartment
        self.__showData()

        #private method
    def __showData(self):
        print("Name  = {}".format(self.__name))
        print("Salary = {} THB".format(self.__salary))
        print("Department = {}".format(self.__department))

obj1 = Employee("Genji",30000,"DPS")
