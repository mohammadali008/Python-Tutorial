# Dictionary Data Type in Python

# Dictionary declaration
person = {"name": "Ali", "age": 25, "city": "Tehran"}
empty_dict = {}

# Accessing values
print(person["name"])        # 'Ali'
print(person.get("age"))     # 25
print(person.get("job", "N/A"))  # 'N/A' if key not found

# Modifying values
person["age"] = 26
person["job"] = "Engineer"

# Removing items
del person["city"]
removed = person.pop("job")   # Removes and returns the value
person.clear()                # Remove all items

# Re-declare to continue
person = {"name": "Ali", "age": 25}

# Keys, values, items
print(person.keys())     # dict_keys(['name', 'age'])
print(person.values())   # dict_values(['Ali', 25])
print(person.items())    # dict_items([('name', 'Ali'), ('age', 25)])

# Iterating through dict
for key in person:
    print(key, person[key])

for k, v in person.items():
    print(f"{k} => {v}")

# Dictionary comprehension
squared = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, ..., 4: 16}

# Nested dictionary
students = {
    "Ali": {"age": 20, "grade": "A"},
    "Sara": {"age": 22, "grade": "B"},
}
print(students["Ali"]["grade"])  # 'A'
