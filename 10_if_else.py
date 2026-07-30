"""
TOPIC: If-Else
--------------
Conditional execution. Python uses INDENTATION (not braces) to define
blocks -> this is not optional, it's how Python knows what's inside
the if-block.
"""

age = 20

# 1. Basic if-elif-else
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# 2. Nested if
marks = 85
attendance = 78

if marks >= 60:
    if attendance >= 75:
        print("Eligible for exam")
    else:
        print("Marks ok, but attendance too low")
else:
    print("Not eligible")

# 3. Combining conditions with logical operators (usually cleaner
# than nesting)
if marks >= 60 and attendance >= 75:
    print("Eligible for exam (combined condition)")

# 4. Ternary / conditional expression -> one-line if-else
status = "Pass" if marks >= 40 else "Fail"
print(status)

# 5. Truthy / Falsy values -> Python treats these as False automatically:
# 0, 0.0, "", [], {}, set(), None
name = ""
if name:
    print("Name provided")
else:
    print("Name is empty")   # this runs, empty string is falsy

# 6. match-case (Python 3.10+) -> like switch in other languages
day = 3
match day:
    case 1:
        print("Monday")
    case 2 | 3:            # multiple values with |
        print("Tuesday or Wednesday")
    case _:                 # default case
        print("Some other day")


