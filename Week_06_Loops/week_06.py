# ================= WEEK 6: CONTROL FLOW – LOOPS AND ITERATIONS =================

# Exercise 1: Prime numbers up to a given number
# A prime number has exactly two factors: 1 and itself. The loop checks divisibility.
limit = int(input("Enter a limit: "))

print("Prime numbers:")
for number in range(2, limit + 1):
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")

# Exercise 2: Multiplication table using nested loops
# A nested loop is a loop inside another loop. It is useful for tables and repeated combinations.
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()

# Exercise 3: Simple number guessing game
# The computer chooses a number and the user keeps guessing until the correct value is found.
import random

secret = random.randint(1, 10)

while True:
    try:
        guess = int(input("Guess a number from 1 to 10: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if not 1 <= guess <= 10:
        print("Choose a number from 1 to 10.")
    elif guess == secret:
        print("Correct! You guessed the number.")
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")
