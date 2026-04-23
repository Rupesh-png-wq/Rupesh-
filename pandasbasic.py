import pandas as pd
# Load CSV file
df = pd.read_csv("C:/Users/rupes/OneDrive/Desktop/data.csv")

# Display first few rows
print("First 5 rows:")
print(df.head())

# Basic info about dataset
print("\nDataset Info:")
print(df.info())

# Summary statistics (numerical columns)
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Average salary
print("\nAverage Salary:")
print(df["Salary"].mean())

# Group by Department and get average salary
print("\nAverage Salary by Department:")
print(df.groupby("Department")["Salary"].mean())

# Maximum and minimum salary
print("\nMax Salary:", df["Salary"].max())
print("Min Salary:", df["Salary"].min())