#Creating a class
from dateutil.tz import enfold
from numpy.f2py.crackfortran import real8pattern


class Student:
    name ="karan"

#Creating an object
s1=Student()
print(s1.name)

#Creating constructor
class Car:
    def __init__(self,fullname):
        self.name=fullname
        print("Adding new car to the list: "+fullname)

#Creating Object
car1=Car("Corolla")
print(car1.name)
car2=Car("Mehran")
print(car2.name)
car3=Car("Alto")
print(car3.name)
car4=Car("Cultus")
print(car4.name)

#Using parameterized constructor
class Bird:
    def __init__(self, name):
        self.name=name
        print(f"{self.name} added to the list")
#creating object
bird1=Bird("Peacock")
bird3=Bird("")
bird4=Bird("Pigeon")

#class attributes
class Class:
    class_name="Default"
print(Class.class_name)

#Methods
class Teacher:
    def __init__(self, name):
        self.name=name
        print("Object created: ",name)
    def greet(self):
        print("Hello",self.name)
    def getname(self):
        return self.name
teacher=Teacher("Naveen Kumar")
teacher.greet()
print(teacher.getname())


#Static Mehods
class Student():
    @staticmethod
    def hello():
        print("hello")
Student.hello()

#abstraction
class ggsme:
    def __init__(self):
        self.trials=3
        self.movement=False
    def start(self):
        self.trials-=1
        self.movement=True
        print("Player has started moving")
#All the details written above do the thing but they are hidden
#Ones below are for the user and are essential parts
abc=ggsme()
abc.start()

#use of 'del' keyword
class Student:
    def __init__(self,name):
        self.name=name
s1=Student("Zeeshan")
print(s1)
#after deleting
del s1
#print(s1)  Commented becuase shows error!! Since the object s1 exists no more


#using __ to make an attribute private to restrict its access from outside the class
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    def print_pass(self):
        print(self.__acc_pass)
acc1=Account("12345","abcde")
#Password won't be printed because its private. You can uncomment the line below and check
#print(acc1.__acc_pass)
#But it'll be printed if there's a function within class asking for it. See below:
acc1.print_pass()


#Trying to access private methods from outside the class
class abc:
    __name="Anonymous"
    def __hello(self):
        print("Hello!")
#Trying to call private method hello from outside the class
a=abc()
#a.__hello()   This shows error because we re trying to access a private method from outside the class

#Let's see how can private methods be used
class abc:
    __name="Anonymous"
    def __hello(self,name):
        print("Hello! ",name)
    def welcome(self):
        self.__hello(self.__name)
a=abc()
a.welcome()



#Using inheritance - a pillar of OOP
class Car:
    color="Black"
    @staticmethod
    def start():
        print("Car Started")
    @staticmethod
    def stop():
        print("Car Stopped")
class Toyota(Car):
    def __init__(self,name):
        self.name=name
car1=Toyota("Prius")
car2=Toyota("Fortuner")
#Although Start and Stop are not methods of Toyota Class but since it's a part of the parent class "car", it wont be an issue!!
print(car1.color,car1.name)
car1.start()
print(car2.color,car2.name)
car2.start()



#The inheritance implemented above was a single level inheritance
#Let's now take a look at how can multi level inheritance be used
class Living():
    name="xyz"
    @staticmethod
    def breath():
        print("It breathes!")
    @staticmethod
    def grow():
        print("It grows!")
class Mammals(Living):
    @staticmethod
    def has_hairs():
        print("Has hairs on skin")
class Dog(Mammals):
    def __init__(self,name):
        self.name=name
    def barks(self):
        print("It barks!")

Dog1=Dog("Tommy")
Dog1.breath()



#Lets implement Multiple Inheritance (a child class with multiple parent classes)
class A:
    varA="Welcome to class A"
class B:
    varB="Welcome to class B"
class C(A,B):
    varC="Welcome to class C"
objectc=C()
#We accessing an attribute of both the parent classes through a child class
print(objectc.varA)
print(objectc.varB)



#Lets see the usage of super()method a way to access parent methods with child objects
class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car Started")
    @staticmethod
    def stop():
        print("Car Stopped")
class Toyota(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
t1=Toyota("Prius","electric")
print(t1.name, t1.type)



#Lets take a look at the usage of class methods
class Person:
    name="anonymous"
    @classmethod
    def changeName(cls,name):
        cls.name=name
print(Person.name)
Person.changeName("Rahul")
print(Person.name)



#Lets see the use of property keyword
class Student:
    def __init__(self,eng,urdu,maths):
        self.eng=eng
        self.urdu=urdu
        self.maths=maths
    @property
    def percentage(self):
        return str((self.eng+self.maths+self.urdu) / 3)+"%"
Tahir=Student(89,90,94)
print(Tahir.percentage)
Tahir.maths=76
print(Tahir.percentage)

#Understanding Polymorphism by creating our own Complex Numbers class
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show(self):
        print(self.real,"i + ",self.img,"j")
#Using add dunder function to modify the definition of how "+" works for Complex numbers
    def __add__(self, num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
c1=Complex(1,2)
c2=Complex(4,5)
c1.show()
c2.show()
c3=c1+c2
c3.show()