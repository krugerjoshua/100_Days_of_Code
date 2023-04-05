# This is a guessing game where the user should guess the correct number.
# Importing the random library.
import random

print("Welcome to guess the number game.")
print("Guess the correct number between 0 and 1 000 000")
# These two variables is to show how many attempts a user made and the correct number.
attempts = 0
number = random.randint(1, 1000000)
# This while loop is too run until user has chosen the correct number.
while True:
    user_attempt = int(input(": "))
    if user_attempt == number:
        print(f"Congrats you geussed the correct number! Who would've thought to get it in {attempts} attempts. ;)")
        exit()
    elif user_attempt > number:
        print("Guessed too high!")
        print("Please guess again")
        attempts += 1
        continue
    elif user_attempt < number:
        print("That's too low :(")
        print("Please guess again")
        attempts += 1
        continue
