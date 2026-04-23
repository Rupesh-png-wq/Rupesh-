# Define a custom exception
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    # Raise custom exception
    if age < 18:
        raise InvalidAgeError("You must be at least 18 years old.")

    print("Access granted!")

except InvalidAgeError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Error: Please enter a valid number.")

finally:
    print("This block always executes (finally block).")