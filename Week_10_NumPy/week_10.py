# ================= WEEK 10: INTRODUCTION TO NUMPY =================

# Exercise 1: Create and manipulate NumPy arrays
# NumPy provides an array structure that is useful for numerical work.
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

print("Array:", numbers)
print("First item:", numbers[0])
print("Last two items:", numbers[-2:])

numbers = numbers * 2
print("After multiplication:", numbers)

# Exercise 2: Basic mathematical operations with NumPy
# NumPy performs arithmetic operations directly on arrays.
import numpy as np

numbers = np.array([10, 20, 30])

print("Add 5:", numbers + 5)
print("Multiply by 2:", numbers * 2)
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))

# Exercise 3: Matrix multiplication using NumPy
# The @ operator performs matrix multiplication when the dimensions are compatible.
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

result = A @ B

print(result)
