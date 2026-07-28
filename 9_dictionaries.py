"""
TOPIC: Dictionaries
--------------------
Key-value pairs. MUTABLE, keys must be unique & immutable (str, int, tuple).
This is what you'll use constantly -> think JSON objects.
"""

# 1. Creation
student = {
    "name": "Nishant",
    "course": "MCA",
    "year": 2025
}
print(student)

# 2. Accessing values
print(student["name"])
print(student.get("name"))          # safer -> won't crash if key is missing
print(student.get("grade", "N/A"))  # default value if key doesn't exist
# print(student["grade"])  -> KeyError, key doesn't exist

# 3. Adding / updating
student["year"] = 2026              # update existing key
student["college"] = "GCET"         # add new key
print(student)

# 4. Removing
student.pop("college")              # remove specific key
print(student)

# 5. Looping through a dictionary
for key in student:
    print(key, "->", student[key])

for key, value in student.items():  # cleaner way, unpacks pairs directly
    print(f"{key}: {value}")

print(list(student.keys()))
print(list(student.values()))

# 6. Checking existence
print("name" in student)            # checks KEYS by default
print("Nishant" in student.values())

# 7. Dictionary comprehension
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)

# 8. Nested dictionaries -> very common for real-world data (like JSON)
users = {
    "u1": {"name": "Nishant", "role": "developer"},
    "u2": {"name": "Aman", "role": "designer"}
}
print(users["u1"]["name"])

# 9. update() -> merge another dict in
student.update({"city": "Greater Noida", "year": 2027})
print(student)


