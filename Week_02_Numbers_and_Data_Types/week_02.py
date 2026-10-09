# WEEK 2: NUMBERS, VARIABLES AND DATA TYPES
celsius = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit:", (celsius * 9 / 5) + 32)

age, height, name, is_student = 20, 1.75, "Student", True
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

shape = input("Enter shape (circle, rectangle, triangle): ").lower()
if shape == "circle":
    radius = float(input("Enter radius: "))
    print("Area:", round(3.14159 * radius ** 2, 2) if radius >= 0 else "Radius cannot be negative.")
elif shape == "rectangle":
    length, width = float(input("Enter length: ")), float(input("Enter width: "))
    print("Area:", round(length * width, 2) if length >= 0 and width >= 0 else "Length and width cannot be negative.")
elif shape == "triangle":
    base, height = float(input("Enter base: ")), float(input("Enter height: "))
    print("Area:", round(0.5 * base * height, 2) if base >= 0 and height >= 0 else "Base and height cannot be negative.")
else:
    print("Unknown shape. Choose circle, rectangle or triangle.")
