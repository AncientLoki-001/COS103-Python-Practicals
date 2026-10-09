# ================= WEEK 9: FILE HANDLING AND I/O OPERATIONS =================

from pathlib import Path
import csv

# Resolve data files relative to this script, so the practical works whether
# it is launched from the repository root or from this week's folder.
BASE_DIR = Path(__file__).resolve().parent

# Exercise 1: Count words, lines and characters in a text file.
sample_path = BASE_DIR / "sample.txt"
with sample_path.open("r", encoding="utf-8") as file:
    text = file.read()

lines = text.splitlines()
words = text.split()
characters = len(text)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)

# Exercise 2: Write and read a CSV file.
# The file is saved beside this script, not in the caller's working directory.
rows = [
    ["Name", "Score"],
    ["Ada", 78],
    ["Bola", 65],
]

scores_path = BASE_DIR / "scores.csv"
with scores_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with scores_path.open("r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Exercise 3: Simple student database in a CSV file.
# Records are appended so previous student entries are retained.
students_path = BASE_DIR / "students.csv"
name = input("Enter student name: ").strip()
score = input("Enter score: ").strip()

if not name:
    print("Student name cannot be empty.")
else:
    try:
        numeric_score = float(score)
        if not 0 <= numeric_score <= 100:
            raise ValueError
    except ValueError:
        print("Please enter a valid score from 0 to 100.")
    else:
        with students_path.open("a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([name, score])

        print("Student record saved.")
        with students_path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            print("\nSaved records:")
            for row in reader:
                print(row)
