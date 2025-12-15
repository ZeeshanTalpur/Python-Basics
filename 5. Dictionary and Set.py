#creating a simple dictionary
info={
    "Name" : "Zeeshan",
    "Department" : "Software",
    "University" : "Mehran UET",
    "Age" : 20,
    "ID" : "23SW010"
}

#printing the dictionary
print(info)

#printing specific key value pairs from the dictionary
print(info["Name"], info["ID"])

#creating an empty dictionary
null_dict={}
print(null_dict)

#creating a nested dictionary
tahir={
    "Name" : "Muhammad Tahir",
    "Father Name" : "Muhammad Moosa Dars",
    "Department" : "Software",
    "Batch" : 23,
    "Section" : 1,
    "Results" : {
        "SDA" : {
            "Theory" : "A",
            "Practical" : "B",
        },
        "OS" : {
            "Theory" : "C+",
            "Practical" : "B"
        },
        "CN" : {
            "Theory" : "B+",
            "Practical" : "B+"
        },
        "DWH" : {
            "Theory" : "C"
        },
        "CS" : {
            "Theory" : "A"
        }
    }
}

print(tahir)

#dictionary methods
print(tahir.values())
print(tahir.keys())
print(tahir.items())
print(tahir.get("Name"))

#Update method
dictionary={
    "Name" : "Mustafa",
    "Father Name" : "Shabbir Ahmed Bhurgri"
}
dictionary2={
    "Age" : 20
}
dictionary.update(dictionary2)
print(dictionary)
dictionary.update({"city" : "dadu"})
print(dictionary)
print(dictionary2)

#Creating a Set
set1={1,2,3,3,2,1}
print(set1)

#Creating Empty Set
set2=set()
print(set2)

#Set Methods
set2.add(1)
set2.add(2)
set2.add(1)
set2.add(3)
set2.add(6)
set2.add(7)
set2.add(5)
print(set2)
set2.remove(1)
print("1 Removed :", set2)
set2.pop()
print("Popped random element: ",set2)
set2.clear()
print("set Cleared :",set2)

#Union and Intersection of sets
set3={1,2,3}
set4={3,4,5}
print(set4.union(set3))
print(set4.intersection(set3))

