# ================= WEEK 5: COLLECTIONS – LISTS, TUPLES, SETS, AND DICTIONARIES =================

# Exercise 1: Contact book using a dictionary
# A dictionary stores information as key-value pairs. Here the person's name is the key and the phone number is the value.
contacts = {}

name = input("Enter name: ")
phone = input("Enter phone number: ")

contacts[name] = phone

print("Contact book:", contacts)

# Exercise 2: List and set operations
# Lists keep ordered items, while sets store unique items and support set operations.
numbers = [1, 2, 3, 3, 4]
print("List:", numbers)

numbers.append(5)
print("After append:", numbers)

a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

# Exercise 3: Student names and scores
# The program finds the highest score, calculates the average and sorts the names alphabetically.
students = {
    "Ada": 78,
    "Bola": 65,
    "Chidi": 84,
    "David": 71
}

highest = max(students.values())
average = sum(students.values()) / len(students)
names = sorted(students.keys())

print("Highest score:", highest)
print("Average score:", average)
print("Names:", names)
