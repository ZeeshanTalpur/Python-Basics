#creating a simple function
def heading():
    print("Hello!")
heading()

#creating a uniparameterized function
def greet(name):
    print(f"Hello!, {name}")
name=input("Write your name: ")
greet(name)


#creating a multi-parameterized function
def sum(a,b):
   return a+b
a=int(input("Write 1st number: "))
b=int(input("Write 2nd number: "))
sum=sum(a,b)
print(f"The sum of the 1st and 2nd number is {sum}")


def calc_avg(a,b,c):
    return (a+b+c)/3
a=int(input("Write the 1st number: "))
b=int(input("Write the 2nd number: "))
c=int(input("Write the 3rd number: "))
avg=calc_avg(a,b,c)
print(f"The average of three numbers is {avg}")

#Using recursion in python
def sum(n):
    if(i==1):
        return n;
    else:
        return n+sum(n-1)
