'''
Question:

Using the load_wine dataset from sklearn.datasets, perform the following tasks:

Data Loading and Preparation:

- Load the wine dataset and create a DataFrame with appropriate feature names.
Identify and handle any missing values in the dataset.
Exploratory Data Analysis (EDA):

- Provide a statistical summary of the dataset.
Visualize the distribution of alcohol content across different wine classes.
Dimensionality Reduction:

- Apply Principal Component Analysis (PCA) to reduce the dataset to 2 dimensions.
Plot the first two principal components, coloring the points by their wine class.
Model Building and Evaluation:

- Split the data into training and testing sets.
Train a Support Vector Machine (SVM) classifier on the training data.
Evaluate the model's performance on the test data using appropriate metrics.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

# 1. Data Loading and Preparation
wine = load_wine()
df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
df['target'] = wine.target

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

# 2. Exploratory Data Analysis (EDA)
# Statistical summary
print("\nStatistical summary:\n", df.describe())

# Distribution of alcohol content across different wine classes
plt.figure(figsize=(10, 6))
sns.boxplot(x='target', y='alcohol', data=df)
plt.title('Alcohol Content Distribution by Wine Class')
plt.xlabel('Wine Class')
plt.ylabel('Alcohol Content')
plt.show()

# 3. Dimensionality Reduction
# Standardize the features before applying PCA
from sklearn.preprocessing import StandardScaler
features = df.drop('target', axis=1)
features_standardized = StandardScaler().fit_transform(features)

# Apply PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(features_standardized)
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
pca_df['target'] = df['target']

# Plot the first two principal components
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PC1', y='PC2', hue='target', palette='Set1', data=pca_df)
plt.title('PCA of Wine Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

# 4. Model Building and Evaluation
# Split the data
X_train, X_test, y_train, y_test = train_test_split(features_standardized, df['target'], test_size=0.3, random_state=42)

# Train SVM classifier
svm = SVC(kernel='linear', C=1, random_state=42)
svm.fit(X_train, y_train)

# Predict on test data
y_pred = svm.predict(X_test)

# Evaluation
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
