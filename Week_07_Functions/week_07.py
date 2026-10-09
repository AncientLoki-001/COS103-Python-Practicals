# ================= WEEK 7: FUNCTIONS AND LAMBDA EXPRESSIONS =================

# Exercise 1: Function that squares numbers
# A function groups reusable instructions. This function receives a list and returns the squared values.
def square_numbers(numbers):
    result = []
    for number in numbers:
        result.append(number ** 2)
    return result

values = [1, 2, 3, 4]
print(square_numbers(values))

# Exercise 2: Lambda, map and filter
# lambda creates a small anonymous function. map applies a function to items, while filter keeps items that satisfy a condition.
numbers = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Squares:", squares)
print("Even numbers:", even_numbers)

# Exercise 3: Sort dictionaries using lambda
# The key argument tells sorted() which dictionary value should be used for sorting.
students = [
    {"name": "Ada", "score": 78},
    {"name": "Bola", "score": 65},
    {"name": "Chidi", "score": 84}
]

sorted_students = sorted(students, key=lambda student: student["score"])

for student in sorted_students:
    print(student)
