#Creating a class
class Student:
    name="Karan"

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