import random

DEFAULT_LOW = 1
DEFAULT_HIGH = 10


def main():
    """Menu-driven guessing game with option to change high limit."""
    low = DEFAULT_LOW
    high = DEFAULT_HIGH
    number_of_games = 0
    print("Welcome to the guessing game")
    choice = input("(P)lay, (S)et limit, (D)isplay, (Q)uit: ").upper()
    while choice != "Q":
        if choice == "P":
            play(low, high)
            number_of_games += 1
        elif choice == "S":
            high = set_limit(low)
        elif choice == "D" :
            display_all_number(low ,high)
        else:
            print("Invalid choice")
        choice = input("(P)lay, (S)et limit, (D)isplay, (Q)uit: ").upper()
    print(f"Thanks for playing ({number_of_games} times)!")

def display_all_number (low ,high) :
    """display the number from low to high."""
    for number in range(low, high + 1):
        print(format(number, ",.2f"))

def play(low, high):
    """Play guessing game using current low and high values."""
    secret = random.randint(low, high)
    number_of_guesses = 1
    guess = int(input(f"Guess a number between {low} and {high}: "))
    while guess != secret:
        number_of_guesses += 1
        if guess < secret:
            print("Higher")
        else:
            print("Lower")
        guess = int(input(f"Guess a number between {low} and {high}: "))
    print(f"You got it in {number_of_guesses} guesses!")

def set_limit(low):
    """Set high limit to new value from user input."""
    print("Set new limit")
    new_high = int(input(f"Enter a new high value, above {low}: "))
    while new_high <= low:
        new_high = int(input(f"Enter a new high value, above {low}: "))
    return new_high


main()