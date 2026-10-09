# WEEK 3: COMPARISONS, LOGIC AND CONDITIONALS
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Use a sample only; never enter a real password
password = input("Enter a sample password: ")
has_digit = any(char.isdigit() for char in password)
if len(password) >= 8 and has_digit:
    print("Password is strong.")
elif len(password) >= 6:
    print("Password is moderate.")
else:
    print("Password is weak.")

score = float(input("Enter score (0-100): "))
if score < 0 or score > 100:
    print("Invalid score. Enter a value from 0 to 100.")
else:
    if score >= 70: grade = "A"
    elif score >= 60: grade = "B"
    elif score >= 50: grade = "C"
    elif score >= 45: grade = "D"
    elif score >= 40: grade = "E"
    else: grade = "F"
    print("Grade:", grade)
