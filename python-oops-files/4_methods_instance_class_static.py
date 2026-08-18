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