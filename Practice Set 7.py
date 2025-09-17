#Problem 1 : Write a function to print the length of a list(list is a parameter
def length_of_list(list):
    return len(list)
list1=[1,2,4,5,6,7,9]
length=length_of_list(list1)
print(length)

#Problem 2: Write a function to print the elements of a list in a single line
def print_elements(list):
    for el in list:
        print(el,end=" ")
print_elements(list1)

#Problem 3: Write a function to find the factorial of n (n is the parameter)
def factorial(n):
    if n==1:
        return 1;
    return n*factorial(n-1)
number=int(input("\nWrite the number whose factorial you want: "))
print(factorial(number))

#Problem 4: Write a function to convert USD to INR
def convert(usd):
    return usd*86.25
usd=int(input("Write the amount in USD: "))
print(f"The amount in INR is {convert(usd)}")

#Problem 5: Write a recursive function to calculate the sum of n natural numbers
def sum(n):
    if(i==1):
        return n;
    else:
        return n+sum(n-1)

#Problem 6: Write a recursive function to print the elements of a list, use list and index as a parameter
def list_print(list,idx=0):
    if(idx==len(list)):
        return
    else:
        print(list[idx])
        list_print(list, idx+1)
list=['mango','banana','lychee']
list_print(list)