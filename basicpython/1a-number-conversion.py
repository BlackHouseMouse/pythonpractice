#!/usr/bin/python

# This tutorial will cover the concept of numeric type conversion in Python3.x

# Int
positive_int =55

# Float
negative_float = -2.9987654

# Complex
complex_num = 1j

# Convert from int to float
positive_float = float(positive_int)

# Convert from float to int
negative_int = int(negative_float)

# Convert from int to complex
complex_from_int = complex(positive_int)

print(positive_float)
print(negative_int)
print(complex_from_int)

print(type(positive_float))
print(type(negative_int))
print(type(complex_from_int))