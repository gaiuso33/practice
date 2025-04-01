# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
# seaborn has a built-in iris dataset
iris = sns.load_dataset('iris')

# 1. Basic Data Exploration
print("First 5 rows of the dataset:")
print(iris.head())  # Display first 5 rows of the dataset

print("\nSummary statistics:")
print(iris.describe())  # Summary statistics for numerical columns

print("\nData types and non-null counts:")
print(iris.info())  # Information about the dataset

print("\nCount of each species:")
print(iris['species'].value_counts())  # Count of each species

# 2. Data Visualization

# Pairplot for visualizing relationships between features
sns.pairplot(iris, hue='species')
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.show()

# Boxplot for visualizing distribution of features
plt.figure(figsize=(10, 6))
sns.boxplot(x='species', y='sepal_length', data=iris)
plt.title("Boxplot of Sepal Length by Species")
plt.show()

# Violin plot for visualizing distribution and probability density
plt.figure(figsize=(10, 6))
sns.violinplot(x='species', y='petal_length', data=iris)
plt.title("Violin Plot of Petal Length by Species")
plt.show()

# Histogram for each feature
iris.hist(figsize=(10, 8), bins=20)
plt.suptitle("Histograms of Iris Dataset Features")
plt.show()

# Heatmap for visualizing correlations between numerical features
plt.figure(figsize=(8, 6))
sns.heatmap(iris.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap of Iris Dataset")
plt.show()

# 3. Summary Statistics
print("\nSummary statistics by species:")
print(iris.groupby('species').agg(['mean', 'median', 'std']))  # Summary statistics for each species
