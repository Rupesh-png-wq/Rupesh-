import matplotlib.pyplot as plt

# Sample data
x = ["A", "B", "C", "D"]
y = [10, 20, 15, 25]

# 🔹 Line Graph
plt.figure()
plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()

# 🔹 Bar Graph
plt.figure()
plt.bar(x, y)
plt.title("Bar Graph")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()