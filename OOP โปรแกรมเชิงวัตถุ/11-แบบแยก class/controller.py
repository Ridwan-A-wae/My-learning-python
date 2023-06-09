from accounting import Accounting
from programer import Programer
from sale import Sale

account = Accounting("genji",30000,23)
programer = Programer("Hanzo",35000,0,"MERN Stack")
sale = Sale("Ana",40000,"Bangkok")


account._showData()
programer._showData()
sale._showData()

print("Accounting Salary and bonus per/year ="+str(account._getincome(10000)))
print("Programer Salary and bonus per/year ="+str(programer._getincome()))
print("Sale Salary and bonus per/year ="+str(sale._getincome(20000)))
