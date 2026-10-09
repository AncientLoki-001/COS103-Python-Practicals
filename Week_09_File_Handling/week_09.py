# ================= WEEK 9: FILE HANDLING AND I/O OPERATIONS =================

# Exercise 1: Count words, lines and characters in a text file
# The file is opened in read mode. The contents are then used to count lines, words and characters.
# A sample file is included in this folder. Keep this script and sample.txt together.
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

lines = text.splitlines()
words = text.split()
characters = len(text)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)

# Exercise 2: Write and read a CSV file
# The csv module makes it possible to store rows and read them back later.
import csv

rows = [
    ["Name", "Score"],
    ["Ada", 78],
    ["Bola", 65]
]

with open("scores.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("scores.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Exercise 3: Simple student database in a file
# This basic example stores student records in a CSV file. It demonstrates adding and viewing records.
import csv

filename = "students.csv"

name = input("Enter student name: ")
score = input("Enter score: ")

with open(filename, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([name, score])

print("Student record saved.")

with open(filename, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    print("\nSaved records:")
    for row in reader:
        print(row)
