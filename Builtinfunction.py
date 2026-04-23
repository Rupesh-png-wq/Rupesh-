# List operations 
numbers = [5, 2, 9, 1, 7]

print("List:", numbers)
print("Length of list:", len(numbers))
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("Sum of list:", sum(numbers))
print("Sorted list:", sorted(numbers))


# String operations 
text = "hello world"

print("\nString:", text)
print("Length of string:", len(text))
print("Uppercase:", text.upper())
print("Title case:", text.title())
print("Count of 'o':", text.count('o'))
print("Reversed string:", ''.join(reversed(text)))


# Dictionary operations 
student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85
}

print("\nDictionary:", student)
print("Length of dictionary:", len(student))
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# Using get() built-in method
print("Get age:", student.get("age"))

# Adding a new key-value pair
student["grade"] = "A"
print("Updated dictionary:", student)