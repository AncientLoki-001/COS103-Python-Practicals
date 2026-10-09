# WEEK 6: LOOPS AND ITERATIONS
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
print()

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()

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
