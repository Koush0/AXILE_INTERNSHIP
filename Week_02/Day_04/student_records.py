file = open("students.txt", "w")

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    file.write(name + " - " + marks + "\n")

file.close()

print("Student records saved successfully.")
