# WEEK 5: LISTS, TUPLES, SETS AND DICTIONARIES
contacts = {}
name = input("Enter name: ")
phone = input("Enter phone number: ")
contacts[name] = phone
print("Contact book:", contacts)

numbers = [1, 2, 3, 3, 4]
print("List:", numbers)
numbers.append(5)
print("After append:", numbers)
a, b = {1, 2, 3}, {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

students = {"Ada": 78, "Bola": 65, "Chidi": 84, "David": 71}
print("Highest score:", max(students.values()))
print("Average score:", sum(students.values()) / len(students))
print("Names:", sorted(students.keys()))
