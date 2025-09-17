# Problem 1: Write a program too input two numbers and print their sum
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
sum=a+b
print("The sum of the numbers that you entered is:",sum)

#Problem 2: Write a program to input side of a square and print its area
side=float(input("Enter the length of side of the square:"))
print("The area of a square whose side is",side,"long is",side*side)

# Problem 3: Write a program to input 2 floating numbers and print their average
a=float(input("Enter first floating-point number:"))
b=float(input("Enter second floating-point number:"))
avg=(a+b)/2
print("The average of two floating point numbers",a,"and",b,"is",avg)

# Problem 4: Write a program to input two int numbers a and b. Print True if a is greater than or equal to b. If not, print False.
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(a>=b)