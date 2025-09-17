#Problem 1: Write a program to check if a number is even or odd
num=int(input("Enter a number"))
if(num%2==0):
    print("The number is even")
else:
    print("The number is odd")

#Problem 2: Write a program to find the greatest of three numbers entered by a user
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
num3=int(input("Enter a number"))
if(num1>num2 and num1>num3):
    print(num1," is greatest")
elif(num2>num1 and num2>num3):
    print(num2,"is greatest")
elif(num3>num1 and num3>num2):
    print(num3,"is greatest")
elif(num1==num2 and num2==num3):
    print("All numbers are equal")

#Problem 3: Write a program to check if a number is a multiple of 7 or not?
num=int(input("Enter a number"))
if(num%7==0):
    print("Yes,",num,"is a multiple of 7")
else:
    print("No,",num,"is not a multiple of 7")