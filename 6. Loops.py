#Creating a while loop
i=1
while i<=10:
    print(i)
    i+=1

#Using break and continue statements
i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1

i=1
while i<=10:
    print(i)
    if(i==7):
        break
    i+=1

#creating a for loop
list=[1,3,5,7,9,5,2]
for num in list:
    print(num)
tup=(1,2,3,4,5,6,7,6,5,4,3,2,1)
for num in tup:
    print(num)
str="Hi, Bro How are you doing?"
for char in str:
    print(char)
else:
    print("End")

target=input("Enter the letter to be found in string")
str="Mir Zeeshan Talpur"
for idx,char in enumerate(str):
    if(char==target):
        print(f"{target} found at index:{idx}")
        break
    print(char)
else:
    print(target+" not found!")

for el in range(5):
    print(el)

for el in range(1,5):
    print(el)

for el in range(1,5,2):
    print(el)

