# WEEK 9: FILE HANDLING AND CSV
# Keep sample.txt, scores.csv and students.csv in this folder.
import csv

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()
print("Lines:", len(text.splitlines()))
print("Words:", len(text.split()))
print("Characters:", len(text))

rows = [["Name", "Score"], ["Ada", 78], ["Bola", 65]]
with open("scores.csv", "w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerows(rows)
with open("scores.csv", "r", newline="", encoding="utf-8") as file:
    for row in csv.reader(file):
        print(row)

filename = "students.csv"
name = input("Enter student name: ")
score = input("Enter score: ")
with open(filename, "a", newline="", encoding="utf-8") as file:
    csv.writer(file).writerow([name, score])
print("Student record saved.")
with open(filename, "r", newline="", encoding="utf-8") as file:
    print("\nSaved records:")
    for row in csv.reader(file):
        print(row)
