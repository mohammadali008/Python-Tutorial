# Numeric Data Types in Python

# Integer (int)
x = 10
y = -5
z = 0
print(type(x))  # <class 'int'>

# Float (decimal numbers)
a = 3.14
b = -0.001
c = 1.0
print(type(a))  # <class 'float'>

# Complex numbers
comp1 = 2 + 3j
comp2 = complex(4, -2)
print(type(comp1))  # <class 'complex'>

# Arithmetic operations
add = x + a         # 13.14
sub = x - y         # 15
mul = x * a         # 31.4
div = x / 3         # 3.333...
int_div = x // 3    # 3 (integer division)
mod = x % 3         # 1 (remainder)
power = x ** 2      # 100 (exponentiation)

# Float precision
precise = 0.1 + 0.2  # 0.30000000000000004 (floating point limitation)

# Type conversion
int_from_float = int(5.9)       # 5
float_from_int = float(5)       # 5.0
complex_from_int = complex(7)   # (7+0j)

# Useful numeric functions
print(abs(-10))      # 10 (absolute value)
print(round(3.14159, 2))  # 3.14 (round to 2 decimals)
print(pow(2, 3))      # 8 (2^3)
print(divmod(10, 3))  # (3, 1) -> quotient and remainder

# Working with math module
import math
print(math.sqrt(16))    # 4.0
print(math.ceil(4.2))   # 5
print(math.floor(4.9))  # 4
print(math.pi)          # 3.141592...
print(math.factorial(5))  # 120
