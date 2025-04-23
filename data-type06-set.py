# Set Data Type in Python

# Set declaration
s1 = {1, 2, 3}
s2 = set([3, 4, 5])
s3 = set()  # Empty set (not {} because that's a dict)

# Sets are unordered and have unique elements
s4 = {1, 2, 2, 3}
print(s4)  # {1, 2, 3}

# Adding elements
s1.add(4)
s1.update([5, 6])  # Add multiple

# Removing elements
s1.remove(2)       # Removes 2, raises error if not found
s1.discard(100)    # Removes safely (no error if not found)
popped = s1.pop()  # Removes a random element

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union => {1, 2, 3, 4, 5}
print(a & b)   # Intersection => {3}
print(a - b)   # Difference => {1, 2}
print(a ^ b)   # Symmetric difference => {1, 2, 4, 5}

# Membership test
print(2 in a)     # True
print(10 not in a)  # True

# Set methods
print(len(a))       # Number of elements
print(a.isdisjoint({10, 11}))  # True
print(a.issubset({1, 2, 3, 4}))  # True
print(b.issuperset({4}))        # True

# Iterating over a set
for item in a:
    print(item)
