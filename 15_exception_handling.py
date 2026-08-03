"""
TOPIC: Exception Handling
--------------------------
Handle runtime errors gracefully instead of letting the program crash.
"""

# 1. Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")

# 2. Catching multiple specific exception types
try:
    num = int("abc")
except ZeroDivisionError:
    print("Division error")
except ValueError:
    print("Invalid conversion to int")

# 3. Catching the exception object itself -> to see the actual message
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"Index error occurred: {e}")

# 4. Generic except -> catches ANY exception. Use sparingly, since
# it can hide bugs you didn't expect
try:
    risky_code = 1 / 0
except Exception as e:
    print(f"Something went wrong: {e}")

# 5. else -> runs ONLY if no exception occurred
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print(f"Success, result is {x}")   # this runs

# 6. finally -> ALWAYS runs, error or not (cleanup code, closing files etc.)
try:
    f = "pretend file handle"
    print("Processing file")
except Exception:
    print("Error processing")
finally:
    print("Cleanup happens here regardless")

# 7. Raising your own exceptions
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Caught: {e}")

# 8. Custom exception classes -> for domain-specific errors
class InsufficientBalanceError(Exception):
    """Raised when a withdrawal exceeds the account balance."""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")
    return balance - amount

try:
    withdraw(1000, 5000)
except InsufficientBalanceError as e:
    print(f"Transaction failed: {e}")

