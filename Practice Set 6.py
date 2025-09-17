#Problem 1: Print numbers from 1 to 100
print("Problem 1: ")
i=1
while i<=100:
    print(i)
    i+=1
print("Problem 2: ")

#Problem 2: Print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1

#Problem 3: Print multiplication table of a number n
n=int(input("Enter a number: "))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1

#Problem 4: Print the elements of the following list using a loop [1,4,9,16,25,36,49,64,81,100]
i=1
while i<=10:
    print(i**2)
    i+=1

list=[1,4,9,16,25,36,49,64,81,100]
i=1
while i<len(list):
    print(list[i])
    i+=1

tuple=(1,4,9,16,25,36,49,64,81,100)
target=int(input("Enter number to be searched from the list: "))
i=1
while i<len(tuple):
    if(list[i]==target):
        print("The target number is present at index:",i)
    i+=1

#Problem 5: Print the following elements of a list using for loop
list=[1,4,9,16,25,36,49,64,81,100]
for i in list:
    print(i)

#Problem 6: Search for a target number in the tuple using a for loop
target=int(input("Enter your target: "))

tuple=(1,4,9,16,25,36,49,64,81,100)
index=0
for i in tuple:
    if(i==target):
        print("Target found at index:",index)
    index+=1

#Problem 7: Print numbers from 1 to 100
for el in range(1,101):
    print(el)

#Problem 8: Print numbers from 100 to 1
for el in range(100,0,-1):
    print(el)

#Problem 9: Print multiplication table of number n
n=int(input("Enter the number you want the table of:"))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")

#Problem 10: Write a program to print the sum of first n numbers
limit =int(input("Write the value of n"))
sum=0
i=1
while(i<=limit):
    sum+=i
    i+=1
else:
    print(f"The sum of n natural numbers is {sum}")

#Problem 11: Write a program to find the factorial of a number(using for)
n=int(input("Write the number you want the factorial of:"))
fact=1
for i in range(1,n+1):
    fact*=i
else:
    print(f"The factorial of {n} is {fact}")