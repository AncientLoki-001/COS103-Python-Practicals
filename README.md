# COS 103 Python Practicals

## Weeks 11 and 12

This repository contains the corrected Week 11 and Week 12 practical work for COS 103 (Python).

### Week 11 — Data Analysis
- Loads the supplied Iris dataset with pandas.
- Checks dataset size and missing values.
- Produces summary statistics and species counts.
- Creates three plots:
  - Species count
  - Petal length vs. petal width
  - Sepal length distribution

Files:
- `Week_11_Data_Analysis/week11_iris_analysis.py`
- `Week_11_Data_Analysis/Iris.csv`
- `Week_11_Data_Analysis/graphs/`

### Week 12 — Decision Tree Classification
- Uses the four Iris measurements as features.
- Splits the data into 80% training and 20% testing sets. 
- Trains a Decision Tree classifier.
- Evaluates accuracy, weighted precision, weighted recall, and the confusion matrix.
- Saves a visualization of the trained tree.

Files:
- `Week_12_Decision_Tree/week12_decision_tree.py`
- `Week_12_Decision_Tree/Iris.csv`
- `Week_12_Decision_Tree/decision_tree.png`


### Results
Using `random_state=42` and stratified splitting:
- Accuracy: **0.9333**
- Weighted precision: **0.9333**
- Weighted recall: **0.9333**

### Dataset
The Iris dataset contains 150 records across three species, with 50 records per species.

Source: Kaggle — Iris Species
https://www.kaggle.com/datasets/uciml/iris

### Requirements
```bash
pip install pandas matplotlib scikit-learn
```

Run each Python script from its respective folder.
