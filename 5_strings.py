"""
TOPIC: Strings
--------------
Strings are IMMUTABLE sequences of characters. Every "modification"
method actually returns a NEW string.
"""

s = "Python Programming"

# 1. Indexing & slicing
print(s[0])        # 'P'
print(s[-1])        # 'g' -> negative index from the end
print(s[0:6])       # 'Python' -> slice [start:end), end excluded
print(s[7:])        # 'Programming'
print(s[::-1])   
k= "Nishant Kumar"   # reversed string -> handy trick
print(k[::-1])

# 2. Immutability -> this would fail:
# s[0] = "J"   -> TypeError: 'str' object does not support item assignment
s = "J" + s[1:]     # correct way: build a new string
print(s)

# 3. Common methods
text = "  Hello World  "
print(text.strip())          # remove leading/trailing whitespace
print(text.upper())
print(text.lower())
print(text.strip().replace("World", "Python"))
print("apple,banana,mango".split(","))     # -> list
print("-".join(["a", "b", "c"]))           # opposite of split
print(text.strip().find("World"))          # index of substring, -1 if absent
print(s.startswith("J"), s.endswith("g"))

# 4. Checking content
print("abc123".isalnum())
print("abc".isalpha())
print("123".isdigit())

# 5. Escape characters
print("Line1\nLine2")     # newline
print("Tab\tSeparated")
print("She said \"hello\"")

# 6. Length & concatenation
print(len(s))
print(s + " Language")
print(s * 2)               # repeat

