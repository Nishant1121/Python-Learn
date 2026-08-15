"""
TOPIC: Instance vs Class Attributes
--------------------------------------
Instance attributes -> belong to ONE object (set via self.x in __init__)
Class attributes    -> shared across ALL objects of that class
"""


class Student:
    college = "GCET"          # class attribute -> same for every student

    def __init__(self, name):
        self.name = name       # instance attribute -> unique per object


s1 = Student("Nishant")
s2 = Student("Aman")

print(s1.name, s1.college)
print(s2.name, s2.college)   # same college, different name

# 1. Changing a class attribute through the CLASS affects ALL objects
Student.college = "Galgotias"
print(s1.college)   # updated
print(s2.college)   # also updated -> they share the same class attribute

# 2. But setting it through an INSTANCE creates a new instance
# attribute that just shadows the class one for THAT object only
s1.college = "Different College"
print(s1.college)   # "Different College" -> instance attribute now
print(s2.college)   # "Galgotias" -> unaffected, still uses class attribute
print(Student.college)   # "Galgotias" -> class attribute itself unchanged


# 3. Classic gotcha: MUTABLE class attributes shared across instances
class Team:
    members = []   # DANGER: this list is shared by every Team object!

    def add_member(self, name):
        self.members.append(name)


t1 = Team()
t2 = Team()
t1.add_member("Nishant")
print(t2.members)   # ['Nishant'] -> t2 got it too! They shared one list.


# The fix: initialize mutable attributes inside __init__ instead
class TeamFixed:
    def __init__(self):
        self.members = []   # NEW list created per object

    def add_member(self, name):
        self.members.append(name)


t3 = TeamFixed()
t4 = TeamFixed()
t3.add_member("Nishant")
print(t4.members)   # [] -> correctly empty, independent lists


# 4. A counter using a class attribute -> practical use case
class Employee:
    total_employees = 0   # tracks count across ALL instances

    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1   # increment shared counter


e1 = Employee("A")
e2 = Employee("B")
e3 = Employee("C")
print(Employee.total_employees)   # 3

