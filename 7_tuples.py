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

# 4. Unpacking -> very common and clean pattern
x, y = point
print(f"x={x}, y={y}")

a, b, *rest = (1, 2, 3, 4, 5)   # * grabs the remaining items into a list
print(a, b, rest)

# 5. Methods -> tuples only have 2, since they're immutable
nums = (1, 2, 2, 3, 2)
print(nums.count(2))     # how many times 2 appears
print(nums.index(3))     # first index of value 3

# 6. Why use a tuple over a list?
# - signals intent: "this data won't change"
# - slightly faster & uses less memory than a list
# - can be used as a dictionary key (lists cannot)
locations = {(28.6, 77.2): "Delhi", (25.3, 82.9): "Varanasi"}
print(locations[(25.3, 82.9)])

# 7. Functions returning multiple values -> actually returns a tuple
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([4, 1, 9, 3])
print(lo, hi)
