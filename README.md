# COS 103 Python Practicals

Python practical exercises for COS 103. The repository currently contains the completed Week 11 and Week 12 exercises.

## Project structure

```text
COS103-Python-Practicals/
├── README.md
├── requirements.txt
├── .gitignore
├── Week_11_Data_Analysis/
│   ├── Iris.csv
│   ├── week11_iris_analysis.py
│   └── graphs/
│       ├── iris_species_count.png
│       ├── iris_petal_scatter.png
│       └── iris_sepal_hist.png
└── Week_12_Decision_Tree/
    ├── Iris.csv
    ├── week12_decision_tree.py
    └── decision_tree.png
```

## Week 11 — Iris data analysis

The script uses pandas to inspect the Iris dataset and prints the first rows, dataset dimensions, missing-value counts, summary statistics, and counts by species. It generates three charts:

- `graphs/iris_species_count.png` — number of flowers in each species
- `graphs/iris_petal_scatter.png` — petal length compared with petal width, grouped by species
- `graphs/iris_sepal_hist.png` — distribution of sepal length

Run it from the repository root:

```bash
python Week_11_Data_Analysis/week11_iris_analysis.py
```

## Week 12 — Decision tree classification

The script trains a scikit-learn Decision Tree classifier to predict Iris species from the four flower measurements. It uses an 80/20 train-test split with stratification and a fixed random seed, then prints accuracy, weighted precision, weighted recall, and the confusion matrix. It saves the model diagram as `Week_12_Decision_Tree/decision_tree.png`.

Run it from the repository root:

```bash
python Week_12_Decision_Tree/week12_decision_tree.py
```

With the supplied dataset and current settings, the expected accuracy is approximately **0.9333**. Results may vary if the data or settings change.

## Setup

Python 3.10 or newer is recommended.

Install the dependencies from the repository root:

```bash
python -m pip install -r requirements.txt
```

The scripts load `Iris.csv` relative to their own locations, so they do not depend on the current working directory. Week 11 creates the `graphs/` output folder automatically.

## Dataset

The Iris dataset contains 150 observations across three species. A copy is kept inside each practical's folder so each script can run independently.

Dataset reference: [Iris Species — Kaggle](https://www.kaggle.com/datasets/uciml/iris)

## Scope

Weeks 11 and 12 are currently included in this GitHub repository. Add the earlier practicals in their own week folders when those files are ready.
