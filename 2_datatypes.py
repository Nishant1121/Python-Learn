"""
TOPIC: Data Types
-----------------
Python's built-in types you'll use constantly:
int, float, complex, str, bool, NoneType, and the collection types
(list, tuple, set, dict) which get their own files later.
"""

type(42)                # <class 'int'>
type(3.14)              # <class 'float'>
type("Hello")           # <class 'str'>
type(True)              # <class 'bool'>
print(type(None))              # <class 'NoneType'>

isinstance(3.14, float)  # True
issubclass(int, object)  # True - everything inherits from object

int("42")                # 42
float("3.14")            # 3.14
str(42)                  # "42"
bool(1)                  # True
bool(0)                # False
bool("")               # False — empty string is falsy
bool([])               # False — empty list is falsy
list("abc")              # ["a", "b", "c"]
list((1, 2, 3))        # [1, 2, 3]
set([1, 1, 2, 3])      # {1, 2, 3} — deduplicates

#0, 0.0, "", [], {}, set(), and None are all falsy.Everything else is truthy.

# 1. Numeric types
integer_val = 42
float_val = 3.14
complex_val = 2 + 3j        # rarely used unless doing math/engineering

print(type(integer_val), type(float_val), type(complex_val))

# 2. String
text = "Python"
print(type(text))

# 3. Boolean -> subclass of int internally (True == 1, False == 0)
flag = True
print(flag + 1)             # 2, because True behaves like 1

# 4. NoneType -> represents "no value" (like null in JS)
result = None
print(type(result))

# 5. type() vs isinstance()
print(type(5) == int)
print(isinstance(5, int))   # preferred way to check type

# 6. Type conversion / casting
s = "123"
n = int(s)                  # str -> int
f = float(n)                # int -> float
back_to_str = str(f)        # float -> str
print(n, f, back_to_str, type(back_to_str))

# Careful: this fails
# int("abc")  -> ValueError, can't convert non-numeric string

# 7. Checking mutability (important later)
# int, float, str, tuple -> immutable (can't change in place)
# list, dict, set        -> mutable (can change in place)


# ---------------- PRACTICE ----------------
# TODO 1: take a float 9.8, convert it to int, and print it.
#         Notice: does it round, or does it truncate?
# TODO 2: try bool(0), bool(1), bool(""), bool("hello"), bool([])
#         and predict each result before running
# TODO 3: what happens if you do int("3.5")? Why does it fail
#         when float("3.5") works fine?
