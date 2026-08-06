"""
PROJECT: Calculator
--------------------
Concepts used: functions, if-elif-else, while loop, exception handling,
input/output, type casting.

A menu-driven calculator that keeps running until the user chooses to exit.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def get_number(prompt):
    """Keeps asking until the user enters a valid number. Returns a float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number, try again.")


def show_menu():
    print("\n--- CALCULATOR ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def main():
    operations = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
    }

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice, pick 1-5.")
            continue

        name, operation = operations[choice]
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = operation(num1, num2)
            print(f"{name} result: {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()


# ---------------- STRETCH GOALS ----------------
# 1. Add power (**) and modulus (%) as options 6 and 7
# 2. Keep a history list of past calculations, add an option to view it
# 3. Support chained calculations -> use the previous result as num1
#    for the next operation instead of asking again
