import sqlite3

# Connect to database
conn = sqlite3.connect("company_data.db")
cursor = conn.cursor()

# ===============================
# CREATE TABLES
# ===============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_title TEXT NOT NULL,
    deadline TEXT,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Attendance (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT NOT NULL,
    date TEXT,
    status TEXT
)
""")

# ===============================
# CLEAR OLD DATA (for testing)
# ===============================

cursor.execute("DELETE FROM Employees")
cursor.execute("DELETE FROM Projects")
cursor.execute("DELETE FROM Attendance")

# ===============================
# INSERT SAMPLE DATA
# ===============================

cursor.execute("""
INSERT INTO Employees (full_name, department, salary)
VALUES (?, ?, ?)
""", ("Rohan Mehta", "Software Development", 55000))

cursor.execute("""
INSERT INTO Projects (project_title, deadline, status)
VALUES (?, ?, ?)
""", ("Backend Management System", "2026-03-15", "In Progress"))

cursor.execute("""
INSERT INTO Attendance (employee_name, date, status)
VALUES (?, ?, ?)
""", ("Rohan Mehta", "2026-02-26", "Present"))

conn.commit()

# ===============================
# DISPLAY DATA
# ===============================

print("\n========== EMPLOYEES TABLE ==========")
cursor.execute("SELECT * FROM Employees")
for emp in cursor.fetchall():
    print(f"Employee ID: {emp[0]}")
    print(f"Full Name: {emp[1]}")
    print(f"Department: {emp[2]}")
    print(f"Salary: {emp[3]}")
    print("--------------------------------------")

print("\n========== PROJECTS TABLE ==========")
cursor.execute("SELECT * FROM Projects")
for project in cursor.fetchall():
    print(f"Project ID: {project[0]}")
    print(f"Project Title: {project[1]}")
    print(f"Deadline: {project[2]}")
    print(f"Status: {project[3]}")
    print("--------------------------------------")

print("\n========== ATTENDANCE TABLE ==========")
cursor.execute("SELECT * FROM Attendance")
for record in cursor.fetchall():
    print(f"Record ID: {record[0]}")
    print(f"Employee Name: {record[1]}")
    print(f"Date: {record[2]}")
    print(f"Status: {record[3]}")
    print("--------------------------------------")

conn.close()
