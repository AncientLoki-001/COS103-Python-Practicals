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
 <img width="640" height="480" alt="iris_sepal_hist" src="https://github.com/user-attachments/assets/b22e0999-342f-45d3-8332-9171554a5ba8" />
<img width="640" height="480" alt="iris_petal_scatter" src="https://github.com/user-attachments/assets/442be056-2e8d-48b6-9694-a32e588d8f8b" />
<img width="640" height="480" alt="iris_species_count" src="https://github.com/user-attachments/assets/30727da6-eff2-4dcb-985a-e09c9130b99d" />

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
- <img width="800" height="467" alt="decision_tree" src="https://github.com/user-attachments/assets/51137cd2-560d-4856-b58b-36f5a60fcbcd" />


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
