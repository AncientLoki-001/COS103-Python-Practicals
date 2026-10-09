# COS103 Python Practicals (Weeks 1–12)

This repository contains beginner-friendly Python practicals, with each week in its own folder. Each Week 1–10 folder includes a Python source file and a result snapshot under `results/result_snapshot.svg`.

## Weekly guide

| Week | Topic | Extra files / output |
|---|---|---|
| 1 | Python introduction, arithmetic and calculator | Result snapshot |
| 2 | Numbers, variables, data types and shape areas | Result snapshot |
| 3 | Comparisons, logic, conditionals and grading | Result snapshot |
| 4 | Strings, palindromes and Hangman | Result snapshot |
| 5 | Lists, sets and dictionaries | Result snapshot |
| 6 | Loops, prime numbers, multiplication table and guessing game | Result snapshot |
| 7 | Functions, lambda, map and filter | Result snapshot |
| 8 | Recursion, decorators and Tower of Hanoi | Result snapshot |
| 9 | File handling and CSV | `sample.txt`, `scores.csv`, `students.csv`, result snapshot |
| 10 | NumPy arrays and matrix multiplication | Result snapshot |
| 11 | Iris dataset analysis and graphs | Iris CSV and generated graphs |
| 12 | Decision-tree classification | Iris CSV and decision-tree visualization |

## Requirements

- Python 3.10 or newer is recommended.
- Weeks 1–9 use the Python standard library.
- Week 10 requires NumPy.
- Weeks 11–12 use pandas, matplotlib and scikit-learn.

Install the required packages from the repository root:

```bash
python -m pip install -r requirements.txt
```

## Running a practical

Open a terminal at the repository root and run a week's script. For example:

```bash
python Week_01_Introduction_to_Python/week_01.py
python Week_10_NumPy/week_10.py
```

For Week 9, the script expects `sample.txt`, `scores.csv` and `students.csv` in the same folder as `week_09.py`. The sample files are included. The script rewrites `scores.csv` and appends new records to `students.csv` when you run it.

The result snapshots are sample outputs from representative runs. Interactive programs will display prompts and results based on the values you enter. Do not enter a real password into the Week 3 classroom example.

Weeks 11–12 include the Iris dataset and their own visual outputs.
