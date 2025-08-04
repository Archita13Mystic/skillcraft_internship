# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")
gender_df = pd.read_csv("gender_submission.csv")

# Display basic information
print("Initial Info:\n")
print(train_df.info())
print("\nMissing Values:\n")
print(train_df.isnull().sum())

# Drop 'Cabin' due to too many missing values
train_df.drop(columns=['Cabin'], inplace=True)

# Fill missing Age with median
train_df['Age'].fillna(train_df['Age'].median(), inplace=True)

# Fill missing Embarked with mode
train_df['Embarked'].fillna(train_df['Embarked'].mode()[0], inplace=True)

# Confirm missing values are handled
print("\nAfter Cleaning:\n")
print(train_df.isnull().sum())

# Exploratory Data Analysis
print("\nSurvival Rate by Gender:")
print(train_df.groupby('Sex')['Survived'].mean())

print("\nSurvival Rate by Pclass:")
print(train_df.groupby('Pclass')['Survived'].mean())

# Plot: Survival count
sns.countplot(x='Survived', data=train_df)
plt.title('Survival Count')
plt.show()

# Plot: Survival by Sex
sns.countplot(x='Sex', hue='Survived', data=train_df)
plt.title('Survival by Sex')
plt.show()

# Plot: Age distribution by Survival
sns.histplot(data=train_df, x='Age', hue='Survived', kde=True, bins=30)
plt.title('Age Distribution by Survival')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(train_df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
