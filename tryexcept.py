try:
    # Taking input from user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Division operation
    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers!")

except Exception as e:
    print("Something went wrong:", e)

finally:
    print("Program executed successfully (with or without errors).")