"""
TOPIC: Lists
------------
Ordered, MUTABLE, allow duplicates. The most-used collection in Python.
Think of it like a JS array, but with more built-in methods.
"""

# 1. Creation & indexing
fruits = ["apple", "banana", "mango", "banana"]
print(fruits[0], fruits[-1])
print(fruits[1:3])          # slicing works same as strings

name = ["Nishant", "Sakshi", "Prashant"]
print(name[2],name[-2])
print(name[1:3])          # slicing works same as strings

# 2. Mutability -> unlike strings, this works fine
fruits[0] = "grape"
print(fruits)

