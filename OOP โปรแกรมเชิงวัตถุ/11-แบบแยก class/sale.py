from employee import Employee

class Sale(Employee):
    __departmentName = "Sale"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentName)
        self._area = area

    def _showData(self):
            super()._showData()
            print("Area = "+(self._area))
            print("#########")
