# COS 103 - Week 11: Data Analysis
# Simple analysis of the supplied Iris.csv dataset.

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
iris = pd.read_csv(BASE_DIR / "Iris.csv")

features = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]

print("First five rows:")
print(iris.head())
print("\nDataset shape:", iris.shape)
print("\nMissing values:")
print(iris.isnull().sum())
print("\nSummary statistics:")
print(iris[features].describe())
print("\nSpecies counts:")
print(iris["Species"].value_counts())

output_dir = BASE_DIR / "graphs"
output_dir.mkdir(exist_ok=True)

# Bar chart of the three species
iris["Species"].value_counts().plot(kind="bar")
plt.title("Number of Iris Flowers by Species")
plt.xlabel("Species")
plt.ylabel("Number of Flowers")
plt.tight_layout()
plt.savefig(output_dir / "iris_species_count.png")
plt.close()

# Scatter plot of petal measurements
for species in iris["Species"].unique():
    part = iris[iris["Species"] == species]
    plt.scatter(part["PetalLengthCm"], part["PetalWidthCm"], label=species)
plt.title("Petal Length vs Petal Width")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.legend()
plt.tight_layout()
plt.savefig(output_dir / "iris_petal_scatter.png")
plt.close()

# Histogram of sepal length
plt.hist(iris["SepalLengthCm"], bins=10)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(output_dir / "iris_sepal_hist.png")
plt.close()

print("\nWeek 11 complete. The three graphs are in the graphs folder.")
