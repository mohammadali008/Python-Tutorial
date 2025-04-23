# Tuple Data Type in Python

# Tuple declaration
t1 = (1, 2, 3)
t2 = ("a", "b", "c")
t3 = (1, "hello", 3.14)
t4 = ()               # Empty tuple
t5 = (5,)             # Single-element tuple (needs comma)

# Accessing elements
print(t1[0])          # 1
print(t2[-1])         # 'c'
print(t3[1:3])        # ('hello', 3.14)

# Tuples are immutable
# t1[0] = 100  # ❌ Error: 'tuple' object does not support item assignment

# Tuple unpacking
a, b, c = t1
print(a, b, c)        # 1 2 3

# Nesting tuples
nested = ((1, 2), (3, 4))
print(nested[1][0])   # 3

# Tuple methods
print(t1.count(2))    # 1
print(t1.index(3))    # 2

# Length of tuple
print(len(t1))        # 3

# Using tuples in sets and dict keys (hashable)
my_set = {t1, (4, 5)}
my_dict = {("name", "Ali"): 25}

# Iterating through a tuple
for item in t2:
    print(item)

# Creating tuple from list
lst = [10, 20, 30]
tpl = tuple(lst)
print(tpl)            # (10, 20, 30)
