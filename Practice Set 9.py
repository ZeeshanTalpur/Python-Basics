#Create student class that takes the name and marks of 3 subjects as arguments in constructor. Then create a method to print the average
from enum import nonmember


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(f"Hello {self.name} ! your average score is {sum/3} !!")
s1=Student("Zeeshan",[12,13,15])
s1.avg()


#Create account class with 2 attributes - balance and account no
#Create methods for debit, credit, and printing the balance
class Account:
    def __init__(self,account_number):
        self.balance=10000
        self.account_number=account_number
    def credit(self,amount):
        self.balance+=amount
        print("An amount of ",amount," credited to ",self.account_number)
    def debit(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print("an amount of ",amount," debited from ",self.account_number)
    def check_balance(self):
        print(self.balance)

account=input("Enter your account number: ")
acc=Account(account)
acc.credit(12000)
acc.debit(4500)
acc.check_balance()

 #Create a circle class to create a circle with radius r using the constructor
 #Define an Area() method of the class which calculates the area of the circle
 #Define a Perimeter() method of the class which calculates the perimeter of the circle
class Circle:
    def __init__(self,r):
        self.r=r
    def Area(self):
        return 3.14*(self.r)**2
    def Perimeter(self):
        return 2*3.14*self.r
c1=Circle(3)
print(c1.Area())
print(c1.Perimeter())

#Define an Employee class with attributes role, dept, and salary. The class should have a show details() method
#Create an Engineer class that inherits properties from Employee class and has additional attributes name and age
class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def showDetails(self):
        print(f"Employee Details:\nRole: {self.role}\nDept: {self.dept}\nSalary: {self.salary}")
class Engineer(Employee):
    def __init__(self,name,age,role,dept,salary):
        self.name=name
        self.age=age
        super().__init__(role,dept,salary)
e1=Engineer("Ali",89,"Sr. Engineer","Technical",750000)
e1.showDetails()


#Create a class order which stores items and its price
#Use dunder function __gt__() to convey that :
#   order1 > order2  if  price of order1 > price of order2
class Order:
    def __init__(self,item, price):
        self.item=item
        self.price=price
    def __gt__(self, other):
        return self.price > other.price
o1=Order("Dampukht",4500)
o2=Order("Chai ka cut", 40)
if(o1>o2):
    print(f"Serve {o1.item} first")
else:
    print(f"Serve {o2.item} first")
