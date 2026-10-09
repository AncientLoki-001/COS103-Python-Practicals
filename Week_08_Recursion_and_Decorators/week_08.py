# ================= WEEK 8: ADVANCED FUNCTIONS AND RECURSION =================

# Exercise 1: Recursive factorial
# Recursion happens when a function calls itself. The base case stops the recursion.
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is only defined here for non-negative integers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))

# Exercise 2: Simple decorator for logging
# A decorator can add an extra action before or after another function runs.
def log_call(function):
    def wrapper():
        print("Function is about to run.")
        function()
        print("Function has finished.")
    return wrapper

@log_call
def greet():
    print("Hello from COS103.")

greet()

# Exercise 3: Tower of Hanoi
# The recursive solution moves smaller stacks first, then moves the largest disk, and finally moves the smaller stack again.
def hanoi(n, source, helper, target):
    if n <= 0:
        return
    if n == 1:
        print("Move disk from", source, "to", target)
        return

    hanoi(n - 1, source, target, helper)
    print("Move disk from", source, "to", target)
    hanoi(n - 1, helper, source, target)

hanoi(3, "A", "B", "C")
