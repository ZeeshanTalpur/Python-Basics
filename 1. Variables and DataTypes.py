a5="Me"
a1=2
a2=3.75
a3=None
a4=True

print(a5,a1,a2,a3,a4)
print(type(a1))
print(type(a2))
print(type(a3))
print(type(a4))
print(type(a5))

# Arithmetic Operators
a=5
b=2
print("sum",a+b)
print("difference",a-b)
print("product",a*b)
print("true quotient",a/b)
print("floor quotient",a//b)
print("remainder",a%b)
print("exponent",a**b)

# Relational Operators
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

#Assignment Operators
a=10
print(a)
a+=10
print(a)
a-=10
print(a)
a*=10
print(a)
a/=10
print(a)
a%=10
print(a)
a=10
a**=10
print(a)

#Logical Operators
print(not a==b)
print(a>=b and a>b)
print(a<b or a==b)

#Type Conversion
a=6.25
b=2
sum=a+b
print(sum)
print(type(sum))

#Type Casting
a="9"
b=2
print(type(a))
print(int(a)+b)
print(type(a))
a=int(a)
print(a+b)
print(type(a))

# Taking Inputs
age=input("Enter your age:")
print(age)
print(type(age))
#Default data type for input is str so casting the type while input
age=int(input("Enter your age:"))
print(age)
print(type(age))

