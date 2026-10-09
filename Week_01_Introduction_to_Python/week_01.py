# ================= WEEK 1: INTRODUCTION TO PYTHON =================

# Exercise 1: Printing a simple message
# This introduces the print() function and basic Python syntax.
print("Amigos! I am practicing python programming.")

# Exercise 2: Arithmetic operations
# Python can perform addition, subtraction, multiplication, division, integer division, modulus and powers.
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

# Exercise 3: Simple calculator
# The user enters two numbers and an operator. The if statements choose the required calculation.
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        result = "Error: division by zero is not allowed."
    else:
        result = num1 / num2
else:
    result = "Invalid operator. Please use +, -, * or /."

print("Result:", result)
