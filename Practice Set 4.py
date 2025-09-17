#Problem 1: Write a program that asks the user to write names of his/her 3 fav movies and store them in a list
movie1=input("Write the name of 1st fav movie")
movie2=input("Write the name of 2nd fav movie")
movie3=input("Write the name of 3rd fav movie")
movies=[movie1,movie2,movie3]
print(movies)

#Problem 2: Write a program to check if a list contains a pallindrome of elements
list=[1,2,3,2,1]
dup=list.copy()
dup.reverse()
if(dup==list):
    print("It is a pallindrome")

#Problem 3: Write a program to find the number of "A" grade students in a tuple
grades=('C','A','B','C','A','A','F')
print(grades.count('A'))

#Problem 4: Store above values in a list and sort them from A to D
gradeslist=[grades[0], grades[1], grades[2], grades[3], grades[4], grades[5], grades[6]]
gradeslist.sort()
print(gradeslist)