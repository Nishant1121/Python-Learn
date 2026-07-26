"""
TOPIC: Sets
-----------
Unordered, MUTABLE, NO duplicates allowed. Great for uniqueness checks
and fast membership testing, plus classic math set operations.
"""

# 1. Creation -> duplicates get silently dropped
nums = {1, 2, 2, 3, 3, 3}
print(nums)                 # {1, 2, 3}

empty_set = set()            # NOT {} -> that creates an empty DICT
empty_dict = {}
print(type(empty_set), type(empty_dict))

# 2. No indexing -> sets are unordered, this fails
# print(nums[0])   -> TypeError

# 3. Adding / removing
nums.add(4)
nums.remove(1)        # raises KeyError if item doesn't exist
nums.discard(99)      # does NOT raise error even if item is absent
print(nums)

# 4. Fast membership check -> much faster than list for large data
big_set = set(range(1000000))
print(999999 in big_set)   # near-instant, unlike a list scan

# 5. Mathematical set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # union -> all unique elements from both
print(a & b)    # intersection -> common elements
print(a - b)    # difference -> in a but not in b
print(a ^ b)    # symmetric difference -> in a or b, NOT both