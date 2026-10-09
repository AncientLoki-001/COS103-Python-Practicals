# WEEK 7: FUNCTIONS AND LAMBDA EXPRESSIONS
def square_numbers(numbers):
    return [number ** 2 for number in numbers]

values = [1, 2, 3, 4]
print(square_numbers(values))

numbers = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Squares:", squares)
print("Even numbers:", even_numbers)

students = [
    {"name": "Ada", "score": 78},
    {"name": "Bola", "score": 65},
    {"name": "Chidi", "score": 84},
]
for student in sorted(students, key=lambda item: item["score"]):
    print(student)
