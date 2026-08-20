"""
TOPIC: Encapsulation
-----------------------
Restricting direct access to some of an object's data, and controlling
how it's read/modified from outside. Python doesn't enforce this as
strictly as Java/C++ -> it's convention-based, but the convention
matters and is expected in real code.
"""


# 1. Public attributes (default) -> accessible from anywhere, no protection
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance   # anyone can do account.balance = -9999


acc = Account("Nishant", 1000)
acc.balance = -500   # nothing stops this, even though it's invalid data
print(acc.balance)


# 2. Protected attributes -> single underscore prefix `_name`
# Convention meaning: "internal use, don't touch from outside the class
# or its subclasses" -> Python does NOT actually block access though
class Account2:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance   # "protected" by convention only


acc2 = Account2("Nishant", 1000)
print(acc2._balance)   # still technically accessible, but you're
                          # signaling "you shouldn't be reaching in here"


# 3. Private attributes -> double underscore prefix `__name`
# Python performs "name mangling": __balance becomes _ClassName__balance
# internally, making accidental external access much harder (not
# impossible, but you have to really mean it)
class Account3:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # "private"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance


acc3 = Account3("Nishant", 1000)
# print(acc3.__balance)          # AttributeError, doesn't exist directly
print(acc3.get_balance())
acc3.deposit(500)
acc3.withdraw(2000)               # blocked -> exceeds balance
print(acc3.get_balance())
print(acc3._Account3__balance)    # the "mangled" name -> works, but
                                    # you're clearly bypassing intent

# 4. @property -> the Pythonic way to control access with clean syntax
# (looks like an attribute, behaves like a method)
class Account4:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):              # getter -> acc4.balance (no parens!)
        return self.__balance

    @balance.setter
    def balance(self, value):        # setter -> acc4.balance = value
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value


acc4 = Account4("Nishant", 1000)
print(acc4.balance)     # calls the getter, looks like a plain attribute
acc4.balance = 2000      # calls the setter, validates before assigning
print(acc4.balance)
# acc4.balance = -50     # raises ValueError, setter blocks it