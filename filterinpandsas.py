import pandas as pd

# Read CSV
df = pd.read_csv("data.csv")

filtered = df[df["Salary"] > 35000]
print("Filtered Data:")
print(filtered)

# Group by Department and find average salary
grouped = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:")
print(grouped)