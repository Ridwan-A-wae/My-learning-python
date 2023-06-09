from employee import Employee

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
