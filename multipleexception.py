try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Division
    result = num1 / num2

    # Accessing list element
    my_list = [10, 20, 30]
    index = int(input("Enter index (0-2): "))
    print("Element:", my_list[index])

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

except IndexError:
    print("Error: List index out of range.")

except Exception as e:
    print("Unknown error occurred:", e)

finally:
    print("Program execution completed.")