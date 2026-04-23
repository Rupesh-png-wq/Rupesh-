import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create sample data using NumPy
data = {
    "Name": ["Aman", "Riya", "Rahul", "Sneha"],
    "Marks": np.array([70, 85, 78, 90])
}

# Create DataFrame using pandas
df = pd.DataFrame(data)

# Basic analysis
print("Data:\n", df)
print("\nAverage Marks:", np.mean(df["Marks"]))
print("Maximum Marks:", np.max(df["Marks"]))

# Plot using matplotlib
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()