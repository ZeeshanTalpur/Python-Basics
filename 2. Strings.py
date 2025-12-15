#3 ways to create a string
str1="I am Zeeshan"
str2='I am Zeeshan'
str3="""I am Zeeshan"""
print(str1)
print(str2)
print(str3)

#concatenation
print(str1+str2+str3)
print(str1+" "+str2+" "+str3)
str4=str1+str2+str3
print(str4)

#length of string
print(len(str1))
print(len(str2))
print(len(str3))

#Using index to access
print(str1[0])
print(str1[3])
print(str1[4])
print(str1[7])

#Slicing
print(str1[0:4])
print(str1[3:])
print(str1[:7])
print(str1[-4:])

#String Functions
str4="my name is Don"
print(str4.endswith("on"))
print(str4.capitalize())
print(str4.replace("Don","Comrade"))
print(str4.find("D"))
print(str4.count("n"))



