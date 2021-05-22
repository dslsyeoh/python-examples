import random

generated_number = random.randint(1, 100)


def handle_input():
    try:
        return int(input("Enter number (1 - 100): "))
    except ValueError:
        print("Error: Invalid input, please try again.")
        return handle_input()


def guess(value):
    while value != generated_number:
        print("Please try again!")
        value = handle_input()
        guess(value)
    print("Bingo! You guessed the correct number!")


number = handle_input()
guess(number)
