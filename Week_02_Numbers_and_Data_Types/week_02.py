# ================= WEEK 2: NUMBERS, VARIABLES, AND BASIC DATA TYPES =================

# Exercise 1: Celsius to Fahrenheit
# The formula is F = (C × 9/5) + 32. The same idea can be reversed to convert Fahrenheit to Celsius.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Exercise 2: Variable assignment and type checking
# Different Python values have different data types. type() shows the type stored in a variable.
age = 20
height = 1.75
name = "Student"
is_student = True

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

# Exercise 3: Area of different shapes
# The program asks for a shape and calculates its area using the appropriate formula.
shape = input("Enter shape (circle, rectangle, triangle): ").lower()

if shape == "circle":
    radius = float(input("Enter radius: "))
    if radius < 0:
        print("Radius cannot be negative.")
    else:
        area = 3.14159 * radius ** 2
        print("Area:", round(area, 2))
elif shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    if length < 0 or width < 0:
        print("Length and width cannot be negative.")
    else:
        area = length * width
        print("Area:", round(area, 2))
elif shape == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    if base < 0 or height < 0:
        print("Base and height cannot be negative.")
    else:
        area = 0.5 * base * height
        print("Area:", round(area, 2))
else:
    print("Unknown shape. Choose circle, rectangle or triangle.")
