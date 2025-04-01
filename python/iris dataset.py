import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display the first few rows and basic information about the dataset
print(df.head(3))
print("\nDataset Info:")
print(df.info(3))

# Calculate and display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Calculate correlation matrix
correlation_matrix = df.drop('species', axis=1).corr()

# Create visualizations

# 1. Pairplot
plt.figure(figsize=(10, 8))
sns.pairplot(df, hue='species')
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.savefig('iris_pairplot.png')
plt.close()

# 2. Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig('iris_correlation_heatmap.png')
plt.close()

# 3. Box Plot
plt.figure(figsize=(12, 6))
df.drop('species', axis=1).boxplot()
plt.title("Box Plot of Iris Features")
plt.savefig('iris_boxplot.png')
plt.close()

# 4. Violin Plot
plt.figure(figsize=(12, 6))
for i, feature in enumerate(iris.feature_names):
    plt.subplot(2, 2, i+1)
    sns.violinplot(x='species', y=feature, data=df)
    plt.title(feature)
plt.tight_layout()
plt.savefig('iris_violinplot.png')
plt.close()

# 5. Histogram
plt.figure(figsize=(12, 8))
df.hist(edgecolor='black')
plt.suptitle("Histograms of Iris Features", y=1.02)
plt.tight_layout()
plt.savefig('iris_histograms.png')
plt.close()

# 6. Scatter Plot of Sepal Length vs Sepal Width
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='species', data=df)
plt.title("Sepal Length vs Sepal Width")
plt.savefig('iris_scatter_sepal.png')
plt.close()

print("\nVisualization images have been saved.")

# Additional analysis: Class distribution
print("\nClass Distribution:")
print(df['species'].value_counts())

# Calculate mean values for each species
print("\nMean Values by Species:")
print(df.groupby('species').mean())