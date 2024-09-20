#--------------------


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

student_names.add("Oliver")
print(student_names)

student_names.remove("Sophia")
print(student_names)

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

x = student_scores["Emma"]
print(x)

student_scores["Oliver"] = 95
print(student_scores)

student_scores.update({"Sophia": 82})
print(student_scores)