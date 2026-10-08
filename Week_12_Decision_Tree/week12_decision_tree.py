# COS 103 - Week 12: Decision Tree Classification
# Simple classification of Iris species using a Decision Tree.

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

BASE_DIR = Path(__file__).resolve().parent
iris = pd.read_csv(BASE_DIR / "Iris.csv")

features = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
X = iris[features]
y = iris["Species"]

# 80% of the data is used for training and 20% for testing.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, average="weighted")
recall = recall_score(y_test, predictions, average="weighted")
matrix = confusion_matrix(y_test, predictions)

print("Accuracy:", round(accuracy, 4))
print("Precision (weighted):", round(precision, 4))
print("Recall (weighted):", round(recall, 4))
print("\nConfusion matrix:")
print(matrix)

# Save a picture of the trained decision tree.
plt.figure(figsize=(12, 7))
plot_tree(model, feature_names=features, class_names=model.classes_, filled=True)
plt.title("Decision Tree for Iris Species Classification")
plt.tight_layout()
plt.savefig(BASE_DIR / "decision_tree.png")
plt.close()

print("\nWeek 12 complete. The decision tree image was saved as decision_tree.png.")
