"""
TOPIC: Modules
--------------
A module is just a .py file containing code you can reuse elsewhere.
Python also ships with a huge standard library of ready-made modules.
"""

# 1. Importing an entire module
import math
print(math.sqrt(16))
print(math.pi)

# 2. Importing specific things from a module
from math import sqrt, pi
print(sqrt(25))

# 3. Importing with an alias -> very common for long/library names
import math as m
print(m.floor(4.7))

# 4. Importing everything (generally avoid this -> pollutes namespace,
# unclear where names came from)
# from math import *

# 5. Other commonly used standard library modules
import random
print(random.randint(1, 10))        # random int between 1 and 10
print(random.choice(["a", "b", "c"]))

import datetime
today = datetime.date.today()
print(today)

import os
print(os.getcwd())                   # current working directory

# 6. Creating your own module
# Suppose you have a file called `helpers.py` in the same folder with:
#
#   def greet(name):
#       return f"Hello, {name}!"
#
# You'd use it here as:
#   import helpers
#   print(helpers.greet("Nishant"))

# 7. dir() -> lists everything available inside a module
print(dir(math)[:10])   # first 10 names, just to peek

# 8. __name__ == "__main__" -> lets a file behave differently when run
# directly vs when imported into another file. Standard pattern:

def main():
    print("This only runs when the file is executed directly")

if __name__ == "__main__":
    main()
# If this file gets imported elsewhere with `import 14_modules`,
# main() will NOT auto-run -> only runs on direct execution.

