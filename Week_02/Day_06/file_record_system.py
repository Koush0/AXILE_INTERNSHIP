while True:
    print("\n1. Add Record")
    print("2. View Records")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        file = open("records.txt", "a")
        file.write(name + " - " + marks + "\n")
        file.close()
        print("Record saved.")

    elif choice == "2":
        try:
            file = open("records.txt", "r")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("No records found.")

    elif choice == "3":
        break

    else:
        print("Invalid choice")
