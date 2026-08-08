"""
PROJECT: Number Guess Game
---------------------------
Concepts used: random module, while loop, if-else, exception handling,
functions, f-strings.

The computer picks a random number in a range, user has limited
attempts to guess it, gets "higher/lower" hints each time.
"""

import random


def get_guess(low, high):
    """Keeps asking until user enters a valid integer within range."""
    while True:
        try:
            guess = int(input(f"Guess a number between {low} and {high}: "))
            if guess < low or guess > high:
                print(f"Stay within {low}-{high}.")
                continue
            return guess
        except ValueError:
            print("Enter a whole number, not text.")


def play_round(low=1, high=100, max_attempts=7):
    target = random.randint(low, high)
    attempts = 0

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        guess = get_guess(low, high)
        attempts += 1

        if guess == target:
            print(f"Correct! You got it in {attempts} attempt(s).")
            return True
        elif guess < target:
            print("Think higher!")
        else:
            print("Think lower!")

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"{remaining} attempt(s) left.\n")

    print(f"Out of attempts! The number was {target}.")
    return False


def main():
    print("=== NUMBER GUESSING GAME ===")
    wins = 0
    rounds = 0

    while True:
        rounds += 1
        if play_round():
            wins += 1

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            break

    print(f"\nFinal score: {wins}/{rounds} rounds won.")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
