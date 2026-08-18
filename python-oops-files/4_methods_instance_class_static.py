"""
TOPIC: Methods (Instance, Class, Static)
-------------------------------------------
Instance methods -> operate on ONE object, take `self`, most common
Class methods     -> operate on the CLASS itself, take `cls`
Static methods    -> don't need self OR cls, just live inside the class
                      for organizational purposes
"""


class Employee:
    total_employees = 0
    company_name = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    # 1. Instance method -> needs a specific object's data (self)
    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name}'s new salary: {self.salary}")

    # 2. Class method -> works with the class itself, not one object
    # `@classmethod` decorator + `cls` as first parameter (like self,
    # but refers to the CLASS, not an instance)
    @classmethod
    def get_total_employees(cls):
        return cls.total_employees

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name   # affects ALL employees

    # 3. Static method -> doesn't touch self or cls at all, it's just
    # a utility function that logically belongs with this class
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0


e1 = Employee("Nishant", 50000)
e2 = Employee("Aman", 60000)

e1.give_raise(5000)                          # instance method
print(Employee.get_total_employees())         # class method -> 2
print(Employee.is_valid_salary(-100))         # static method -> False

# 4. classmethod used as an ALTERNATE CONSTRUCTOR -> very common pattern
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # computes age, then calls the normal constructor
        age = 2026 - birth_year
        return cls(name, age)   # cls(...) == Student(...)

    def __str__(self):
        return f"{self.name}, age {self.age}"


s1 = Student("Nishant", 22)                       # normal way
s2 = Student.from_birth_year("Aman", 2003)         # alternate constructor
print(s1)
print(s2)


