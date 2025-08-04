# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Load datasets
df1 = pd.read_csv("bank-full.csv", sep=';')
df2 = pd.read_csv("bank-additional-full.csv", sep=';')

# Display shapes before combining
print("Shape of bank-full.csv:", df1.shape)
print("Shape of bank-additional-full.csv:", df2.shape)

# Align columns and concatenate both datasets
common_cols = df1.columns.intersection(df2.columns)
df_combined = pd.concat([df1[common_cols], df2[common_cols]], ignore_index=True)

print("Combined Dataset Shape:", df_combined.shape)

# Check for missing values
print("\nMissing Values:\n", df_combined.isnull().sum())

# Encode categorical columns
le = LabelEncoder()
cat_cols = df_combined.select_dtypes(include='object').columns

for col in cat_cols:
    df_combined[col] = le.fit_transform(df_combined[col])

# Separate features and target
X = df_combined.drop('y', axis=1)
y = df_combined['y']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Train Decision Tree
clf = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=42)
clf.fit(X_train, y_train)

# Predictions
y_pred = clf.predict(X_test)

# Evaluation
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Decision Tree Visualization
plt.figure(figsize=(20,10))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=["No", "Yes"])
plt.title("Decision Tree for Customer Purchase Prediction (Combined Data)")
plt.show()
