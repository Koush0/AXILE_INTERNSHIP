students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        students[name] = marks
        print("Student added successfully.")

    elif choice == "2":
        print("Student Records:")
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == "3":
        break

    else:
        print("Invalid choice!")
