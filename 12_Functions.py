"""
TOPIC: Functions
----------------
Reusable blocks of code. Defined with `def`, called by name().
"""

# 1. Basic function
def greet():
    print("Hello!")

greet()

# 2. Parameters & return values
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

# 3. Default parameter values
def power(base, exponent=2):    # exponent is optional
    return base ** exponent

print(power(4))          # uses default -> 16
print(power(4, 3))       # overrides default -> 64

# 4. Keyword arguments -> order doesn't matter if named
def introduce(name, age):
    print(f"{name} is {age} years old")

introduce(age=22, name="Nishant")

# 5. *args -> accept any number of positional arguments (as a tuple)
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4, 5))

# 6. **kwargs -> accept any number of keyword arguments (as a dict)
def print_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_details(name="Nishant", role="developer", city="Greater Noida")

# 7. Docstrings -> document what a function does (visible via help())
def divide(a, b):
    """Returns a divided by b. Raises ZeroDivisionError if b is 0."""
    return a / b

print(divide.__doc__)

# 8. Lambda -> small anonymous one-line function
square = lambda x: x ** 2
print(square(5))

# commonly used with sort/map/filter
nums = [5, 2, 8, 1]
nums.sort(key=lambda x: -x)   # sort descending using a lambda
print(nums)

# 9. Recursion -> a function calling itself, needs a base case
def factorial(n):
    if n == 0:            # base case -> stops the recursion
        return 1
    return n * factorial(n - 1)

print(factorial(5))
