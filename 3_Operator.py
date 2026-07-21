"""
TOPIC: Operators
----------------
Arithmetic, comparison, logical, assignment, bitwise, identity, membership.
"""

# 1. Arithmetic
a, b = 17, 5
print(a + b, a - b, a * b, a / b)   # / always gives float
print(a // b)                        # floor division -> 3
print(a % b)                         # modulus -> 2
print(a ** b)                        # exponent -> 17^5

# 2. Comparison -> always return bool
print(a > b, a == b, a != b, a <= b)

# 3. Logical
is_adult = True
has_id = False
print(is_adult and has_id)   # both must be True
print(is_adult or has_id)    # at least one True
print(not is_adult)          # flips it

# 4. Assignment operators (shorthand)
count = 10
count += 1   # same as count = count + 1
count -= 2
count *= 3
print(count)

# 5. Bitwise (works on binary representation of ints)
x, y = 6, 3       # 110 and 011 in binary
print(x & y)       # AND -> 010 -> 2
print(x | y)       # OR  -> 111 -> 7
print(x ^ y)       # XOR -> 101 -> 5
print(x << 1)      # left shift -> 12
print(x >> 1)      # right shift -> 3

# 6. Identity operators -> is / is not
# Checks if two variables point to the SAME object in memory,
# NOT whether values are equal (that's ==)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)   # True -> same values
print(list1 is list2)   # False -> different objects in memory

# 7. Membership operators -> in / not in
fruits = ["apple", "banana", "mango"]
print("banana" in fruits)
print("grape" not in fruits)


n = 15
if n % 3 == 0 and n % 5 == 0:
    print(f"{n} is divisible by both 3 and 5") #here, I used an f-string to format the output.
    print("Is divisible by both 3 and 5") 