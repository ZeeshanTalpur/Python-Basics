#Problem 1: Create a new file "practice.txt" using python Add some data to it
with open("practice.txt","w")as f:
    f.write("Hi everyone\nWe are learning File I/O\nusing Java.\nI like programming in Java")

#Problem 2: Write a function that replaces all occurences of "java" with "python" in above file
with open("practice.txt","r")as f:
    data=f.read()
new_data=data.replace("Java","Python")
with open("practice.txt","w")as f:
    f.write(new_data)

#Problem 3:"See f the word learning exists in the file or not
with open("practice.txt","r")as f:
    data=f.read()
    if("learning"in data):
        print("Found")
    else:
        print("Not Found")

#Problem 4:Write a program to find in which line of the file does the word "learning" exist first
def check_line():
    data=True
    with open("practice.txt","r")as f:
        line_number=1
        while data:
           data=f.readline()
           if "learning" in data:
               print(f"Word found in line number :{line_number}")
               break
           line_number+=1
check_line()

#Problem 5: From a file containing numbers separated by commas, find the count of even numbers
with open("numbers.txt","r")as f:
    data=f.read()
    nums=data.split(",")
    count=0
    for val in nums:
        if(int(val)%2==0):
            count+=1
    print(count)

