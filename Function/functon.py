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

# ------------//

def welcome():
 print("Welcome to Python Programming")


welcome()
welcome()
welcome()

num = 100
def temp_f_to_c():
    calc = (num - 32) * 5/9
    print(calc)    

temp_f_to_c()    


def temp_f_to_c(num):
    calc = (num-32)*5/9
    print(calc)


temp_f_to_c(100)
temp_f_to_c(102)
temp_f_to_c(212)


def area(length,width):
    print( "Area Is",length*width)

area(100,50)   
area(100,100)   
area(100,250)   
