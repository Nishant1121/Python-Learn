"""
PROJECT: Password Generator
-----------------------------
Concepts used: string module, random module, functions, sets/lists,
input validation, f-strings.

Generates a random password based on length and which character
types the user wants included.
"""

import random
import string


def build_char_pool(use_upper, use_lower, use_digits, use_symbols):
    pool = ""
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
    return pool


def generate_password(length, pool):
    return "".join(random.choice(pool) for _ in range(length))


def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Please enter y or n.")


def get_length():
    while True:
        try:
            length = int(input("Password length (min 4): "))
            if length < 4:
                print("Length must be at least 4 for a decent password.")
                continue
            return length
        except ValueError:
            print("Enter a whole number.")


def main():
    print("=== PASSWORD GENERATOR ===")

    length = get_length()
    use_upper = get_yes_no("Include uppercase letters? (y/n): ")
    use_lower = get_yes_no("Include lowercase letters? (y/n): ")
    use_digits = get_yes_no("Include digits? (y/n): ")
    use_symbols = get_yes_no("Include symbols? (y/n): ")

    pool = build_char_pool(use_upper, use_lower, use_digits, use_symbols)

    if not pool:
        print("You didn't select any character type, defaulting to letters+digits.")
        pool = string.ascii_letters + string.digits

    password = generate_password(length, pool)
    print(f"\nGenerated password: {password}")


if __name__ == "__main__":
    main()


# in this code there is some output bug... want to correct it. The output is not coming properly. I want to correct it.