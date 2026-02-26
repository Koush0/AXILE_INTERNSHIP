import sqlite3

# Connect to database
conn = sqlite3.connect("simple.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

conn.commit()

# ===============================
# CREATE
# ===============================
cursor.execute("INSERT INTO Person (name, age) VALUES (?, ?)",
               ("koush", 20))
conn.commit()
print("Person added.\n")

# ===============================
# READ
# ===============================
print("Current Records:")
cursor.execute("SELECT * FROM Person")
for row in cursor.fetchall():
    print(row)

# ===============================
# UPDATE
# ===============================
cursor.execute("UPDATE Person SET age = ? WHERE name = ?",
               (22, "koush"))
conn.commit()
print("\nAge updated.\n")

print("After Update:")
cursor.execute("SELECT * FROM Person")
for row in cursor.fetchall():
    print(row)

# ===============================
# DELETE
# ===============================
cursor.execute("DELETE FROM Person WHERE name = ?",
               ("Riya",))
conn.commit()
print("\nPerson deleted.\n")

print("Final Records:")
cursor.execute("SELECT * FROM Person")
for row in cursor.fetchall():
    print(row)

conn.close()
