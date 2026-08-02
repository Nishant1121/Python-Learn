"""
TOPIC: Scope
------------
Where a variable is accessible from. Python follows the LEGB rule:
Local -> Enclosing -> Global -> Built-in (search order when looking
up a name).
"""

# 1. Local scope -> variable only exists inside the function
def my_func():
    local_var = "I only exist inside my_func"
    print(local_var)

my_func()
# print(local_var)   -> NameError, doesn't exist outside the function

# 2. Global scope -> variable defined outside any function
global_var = "I exist everywhere in this file"

def show_global():
    print(global_var)   # can READ a global variable freely

show_global()

# 3. The gotcha: you CANNOT modify a global variable from inside a
# function without the `global` keyword
counter = 0

def increment_wrong():
    counter = counter + 1   # UnboundLocalError! Python treats counter
                              # as local here because it's being assigned
# increment_wrong()   # uncomment to see the error

def increment_correct():
    global counter            # tells Python: use the outer `counter`
    counter += 1

increment_correct()
print(counter)   # 1

# 4. Enclosing scope -> a nested function can read (but not modify,
# without `nonlocal`) the enclosing function's variables
def outer():
    message = "outer message"

    def inner():
        print(message)   # reads from enclosing scope

    inner()

outer()

# 5. nonlocal -> lets an inner function MODIFY an enclosing (not global)
# variable. Common in closures.
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter_fn = make_counter()
print(counter_fn())   # 1
print(counter_fn())   # 2
print(counter_fn())   # 3

# 6. Built-in scope -> names Python provides automatically
# (print, len, range, etc.) -> lowest priority in lookup order


