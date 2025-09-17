# Creating a list
marks=[1,445,642,1001]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks)

#modifying a list
marks[0]=577
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])

#list slicing
print(marks[0:1])
print(marks[0:2])
print(marks[:3])
print(marks[2:])

#list methods
print("Append 234 to the end")
marks.append(234)
print(marks)
print("Reverse the list")
marks.reverse()
print(marks)
print("Sort in AScending Order")
marks.sort()
print(marks)
print("Sort in descending order")
marks.sort(reverse=True)
print(marks)
print("Insert 454 to the list at index 2")
marks.insert(2,454)
print(marks)
print("remove 445 from the list")
marks.remove(445)
print(marks)
print("Delete 4")
marks.pop(4)
print(marks)

#creating tuples
tup=(1,2,3,4)
print(tup)
print(type(tup))

#accessing distinct elements in a tuple
print(tup[0])
print(tup[3])

#tuple methods
print(tup.index(2))
print(tup.count(4))