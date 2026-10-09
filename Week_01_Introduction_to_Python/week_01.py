# WEEK 1: INTRODUCTION TO PYTHON
print("Amigos! I am practicing python programming.")

# Arithmetic operations
a, b = 10, 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

# Simple calculator
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
    result = "Error: division by zero is not allowed." if num2 == 0 else num1 / num2
else:
    result = "Invalid operator. Please use +, -, *, or /."
print("Result:", result)
