"""
TOPIC: Input & Output
----------------------
Getting data from the user and printing output in different formats.
"""

# 1. print() basics
print("Nishant", "Kumar")                     # default separator = space
print("Nishant", "Kumar", "122", sep="-")             # custom separator
print("Loading", end="...")                  # custom end (default is \n)
print("Done")

# 2. input() -> ALWAYS returns a string, no matter what the user types
name = input("Enter your name: ")
print("Hello, " +name) # , can also be used to separate strings in print() instead of concatenation


# 3. Type casting input immediately (very common pattern)
# age = int(input("Enter your age: "))
age = 22  # simulated
print("Next year you'll be", age + 1)

# 4. String formatting -> 3 ways, f-strings is the modern standard

city = "Greater Noida"
temp = 34.567

# old style (%)
print("City: %s, Temp: %.1f" % (city, temp))

# .format()
print("City: {}, Temp: {:.1f}".format(city, temp))

# f-string (Python 3.6+, use this by default)
print(f"City: {city}, Temp: {temp:.1f}")

# 5. f-strings can hold expressions directly
x = 5
print(f"x squared is {x ** 2}")

# 6. Reading multiple values in one line (common in coding tests)
# a, b = map(int, input("Enter two numbers: ").split())
a, b = map(int, "10 20".split())  # simulated
print(a + b)


# ---------------- PRACTICE ----------------
# TODO 1: take user's name and age via input(), print:
#         "Nishant, you'll be eligible to vote in X years" (if under 18)
# TODO 2: take 3 numbers space-separated on one line, print their average
#         rounded to 2 decimal places using an f-string
# TODO 3: why does `input()` always need int()/float() wrapped around it
#         if you want to do math with the result?
