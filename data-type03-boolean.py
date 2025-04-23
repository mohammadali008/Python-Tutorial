# Boolean Data Type in Python

# Boolean values
is_true = True
is_false = False
print(type(is_true))  # <class 'bool'>

# Boolean expressions
a = 5
b = 3
print(a > b)   # True
print(a == b)  # False
print(a != b)  # True

# Logical operators
x = True
y = False

print(x and y)   # False
print(x or y)    # True
print(not x)     # False

# Boolean with numbers
print(bool(0))       # False
print(bool(1))       # True
print(bool(-10))     # True
print(bool(3.14))    # True

# Boolean with strings
print(bool(""))      # False (empty string)
print(bool("hello")) # True

# Boolean with lists
print(bool([]))      # False (empty list)
print(bool([1, 2]))  # True

# Use in conditions
if a > b:
    print("a is greater than b")

# Boolean from comparison
result = 10 >= 5      # True
print(type(result))   # <class 'bool'>
