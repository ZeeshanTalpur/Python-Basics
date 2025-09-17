#Problem 1: Store Word meanings in a python dictionary
word_meanings={
    "Table" : ("A piece of furniture", "list of facts and figures"),
    "cat" : "a small animal"
}
print(word_meanings)


#Problem 2: You are given list of subjects for students. Each subject requires 1 classroom. What are the total number of classrooms for students
subjects=set()
subjects.add("python")
subjects.add("java")
subjects.add("C++")
subjects.add("python")
subjects.add("javascript")
subjects.add("java")
subjects.add("python")
subjects.add("java")
subjects.add("C++")
subjects.add("C")

print("Total required classrooms:", len(subjects))


#Problem 3: Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value
marks={}
x=int(input("Enter English Marks:"))
marks.update({"English":x})
x=int(input("Enter Urdu Marks:"))
marks.update({"Urdu":x})
x=int(input("Enter Maths Marks:"))
marks.update({"Maths":x})
print(marks)

#Problem 4: Find a way to save 9 and 9.0 separately in a set
a=9
b=9.0
set1={a,b}
print(set1)
