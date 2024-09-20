#--------------------
# Assignment 3: Python Collections
# CIS 103: Introduction to Programming
# Instructor:  Md Ali
# Student Name:  Annie Yung
# Date: 9/20/24

#Creating a list
fruits = ["apple", "banana", "orange", "grape"]
print(fruits)

#removing banana from the list
fruits.remove("banana")
print(fruits)

#adding strawberry to the list
fruits.append("strawberry")
print(fruits)

print()
print()

#Creating a tuple
colors = ("red", "green", "blue", "yellow")
print(colors)

#accessing first element of the tuple
print(colors[0])

#accessing last element of the tuple
print(colors[3])

#attempting to change the value of the 2nd element

colors[1] = "indigo"
print()


#result is that there's a TypeError, the value of a tuple cannot be changed, added, or removed once the tuple has been created

#Creating a set

student_names = {"John", "Emma", "Sophia", "James"}
print(student_names)

#adding Oliver to the set
student_names.add("Oliver")
print(student_names)

#removing Sophia from the set
student_names.remove("Sophia")
print(student_names)

#adding John to the set
student_names.add("John")
print(student_names)

print()
print()

#sets do not allow for duplicate values, so the value of "John" was not added again

#Creating a dictionary
student_scores = {
    "John": 85,
    "Emma": 92,
    "Sophia": 78,
    "James": 89
}

print(student_scores)

#accessing and printing Emma's score
x = student_scores["Emma"]
print(x)

#adding new student Oliver with score of 95
student_scores["Oliver"] = 95
print(student_scores)

#updating Sophia's score to 82 
student_scores.update({"Sophia": 82})
print(student_scores)
