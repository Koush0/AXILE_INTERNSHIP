import sqlite3

# Connect to database
conn = sqlite3.connect("company_data.db")
cursor = conn.cursor()

# ===============================
# CREATE TABLE (if not exists)
# ===============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL
)
""")

conn.commit()

# ===============================
# CRUD FUNCTIONS
# ===============================

# CREATE
def add_employee(name, department, salary):
    cursor.execute("""
    INSERT INTO Employees (full_name, department, salary)
    VALUES (?, ?, ?)
    """, (name, department, salary))
    conn.commit()
    print("Employee added successfully.\n")


# READ
def view_employees():
    cursor.execute("SELECT * FROM Employees")
    records = cursor.fetchall()

    print("\n===== EMPLOYEE RECORDS =====")
    for record in records:
        print(f"ID: {record[0]}")
        print(f"Name: {record[1]}")
        print(f"Department: {record[2]}")
        print(f"Salary: {record[3]}")
        print("-----------------------------")


# UPDATE
def update_salary(emp_id, new_salary):
    cursor.execute("""
    UPDATE Employees
    SET salary = ?
    WHERE emp_id = ?
    """, (new_salary, emp_id))
    conn.commit()
    print("Salary updated successfully.\n")


# DELETE
def delete_employee(emp_id):
    cursor.execute("""
    DELETE FROM Employees
    WHERE emp_id = ?
    """, (emp_id,))
    conn.commit()
    print("Employee deleted successfully.\n")


# ===============================
# TEST OPERATIONS
# ===============================

add_employee("Neha Kapoor", "HR", 40000)
add_employee("Arjun Singh", "Marketing", 45000)

view_employees()

update_salary(1, 50000)

view_employees()

delete_employee(2)

view_employees()

conn.close()
