# WEEK 8: RECURSION AND DECORATORS
def factorial(n):
    if n < 0:
        raise ValueError("Factorial requires a non-negative integer.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))

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
