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