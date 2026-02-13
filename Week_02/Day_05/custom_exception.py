class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise InvalidAgeError("You must be 18 or older.")
    print("Access granted.")
except InvalidAgeError as e:
    print("Custom Exception:", e)
except ValueError:
    print("Please enter a valid number.")
