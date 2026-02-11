student = {
    "name": "Rahul",
    "age": 20,
    "course": "B.E"
}

# Add new item
student["city"] = "Chennai"

# Update value
student["age"] = 21

# Delete item
del student["course"]

print("Updated Dictionary:")
print(student)
