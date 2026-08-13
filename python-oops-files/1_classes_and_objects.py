"""
TOPIC: Classes & Objects
-------------------------
A class is a blueprint. An object (instance) is something built from
that blueprint. This is the foundation everything else in OOP sits on.
"""


# 1. Defining a class
class Car:
    pass   # empty class, just to show the minimum syntax


# 2. Creating objects (instances) from it
car1 = Car()
car2 = Car()
print(type(car1))
print(car1 is car2)   # False -> two separate objects, even if identical class


# 3. A class with attributes set directly on instances
class Student:
    pass


s1 = Student()
s1.name = "Nishant"
s1.course = "MCA"

s2 = Student()
s2.name = "Aman"
s2.course = "BCA"

print(s1.name, s1.course)
print(s2.name, s2.course)
# Notice: s1 and s2 don't share data, each object has its OWN attributes


# 4. Why this matters vs just using a dictionary
# A dict CAN hold similar data:
student_dict = {"name": "Nishant", "course": "MCA"}
# But a class lets you ALSO attach behavior (methods) to that data,
# and enforces a consistent structure across many objects.
# (methods are covered properly in 4_methods.py, this file is just
# about the class/object relationship itself)


class Book:
    def describe(self):
        # `self` refers to the specific object calling this method
        print(f"This book belongs to object at {id(self)}")


b1 = Book()
b2 = Book()
b1.describe()
b2.describe()   # different id -> proves each object is independent



