# WEEK 10: INTRODUCTION TO NUMPY
# Install with: python -m pip install numpy
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])
print("Array:", numbers)
print("First item:", numbers[0])
print("Last two items:", numbers[-2:])
numbers = numbers * 2
print("After multiplication:", numbers)

numbers = np.array([10, 20, 30])
print("Add 5:", numbers + 5)
print("Multiply by 2:", numbers * 2)
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)
