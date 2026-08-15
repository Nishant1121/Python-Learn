"""
TOPIC: Constructor (__init__)
-------------------------------
Setting attributes manually on every object (like in the last file) is
tedious and error-prone. __init__ runs automatically when an object is
created, so you can set attributes at creation time instead.
"""


class Student:
    def __init__(self, name, course):
        # `self.name` creates an attribute ON THIS SPECIFIC OBJECT
        self.name = name
        self.course = course

    def show(self):
        print(f"{self.name} is enrolled in {self.course}")


# 1. Now attributes are passed in at creation -> cleaner, and Python
# WON'T let you forget a required argument
s1 = Student("Nishant", "MCA")
s2 = Student("Aman", "BCA")
s1.show()
s2.show()

# s3 = Student("Missing course")   # TypeError: missing required argument


# 2. Default values for parameters (same idea as regular functions)
class Employee:
    def __init__(self, name, role="Intern"):
        self.name = name
        self.role = role


e1 = Employee("Priya")
e2 = Employee("Rahul", "Developer")
print(e1.name, e1.role)
print(e2.name, e2.role)


# 3. __init__ can also do validation / computed attributes
class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height
        self.area = width * height   # computed once at creation


rect = Rectangle(4, 5)
print(rect.area)

# rect2 = Rectangle(-1, 5)   # raises ValueError immediately


# 4. Common confusion: `self` is NOT a keyword, it's just a convention.
# Python passes the object automatically as the first argument to
# every method -> you could technically name it anything, but never do.
class Demo:
    def __init__(this_thing, value):   # works, but DON'T do this
        this_thing.value = value


d = Demo(10)
print(d.value)

