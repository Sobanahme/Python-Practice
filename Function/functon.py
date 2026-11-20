def Intro():
 print("Hi,My Name is Soban.I am Software Devloper.")

Intro()
Intro()
Intro()

def student(name):
    print("WellCome",name)
student("Soban")    

def calculation_bill(price,quantity):
    total = price*quantity
    print("Total Bill",total)
calculation_bill(10,150)    
calculation_bill(20,650)

def employersalary(salary,bouns,tax):
    gross = salary + bouns
    net = (gross * tax / 100)
    print(net)

employersalary(25000,5000,10)    
employersalary(28000,3000,10)    