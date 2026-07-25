"""
TOPIC: Tuples
-------------
Ordered, IMMUTABLE, allow duplicates. Basically a "locked" list.
Use tuples when data shouldn't change -> coordinates, RGB values,
function returns with multiple values, dict keys, etc.
"""

# 1. Creation
point = (4, 7)
single = (5,)          # NOTE: the comma is REQUIRED for a single-item tuple
not_a_tuple = (5)      # this is just an int in parentheses!
print(type(single), type(not_a_tuple))

# 2. Indexing & slicing -> same as lists
coords = (10, 20, 30, 40)
print(coords[0], coords[-1], coords[1:3])

# 3. Immutability
# coords[0] = 99   -> TypeError, tuples can't be modified after creation

