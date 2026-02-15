while True:
    print("\n1. Check Even/Odd")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        num = int(input("Enter number: "))
        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

    elif choice == "2":
        break

    else:
        print("Invalid choice")
