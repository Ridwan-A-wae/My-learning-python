from employee import Employee

class Accounting(Employee):
    __departmentName = "Accounting"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentName)
        self._age = age
        
    def _showData(self):
            super()._showData()
            print("age = "+str((self._age)))
            print("#########")
