marks=float(input("Enter your marks: "))
if(marks>=90):
    grade='A'
elif(marks>=80 and marks<=90):
    grade='B'
elif(marks>=70 and marks<=80):
    grade='B'
elif(marks>=0 and marks<=70):
    grade='D'
else:
    print("Invalid Marks Entered")

print("Your grade is",grade)
