try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
except ValueError:
    print("Invalid input! Please enter numbers only.")
