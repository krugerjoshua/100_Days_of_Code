# Imported the random module.
import random
# Created a subroutine for the roll dice function. A while loop is also in there for continues play.
def dice_roll(number):
    dice_number = random.randint(1, number)
    print(f"You rolled {dice_number}")
    while True:
        user_input = input("Roll again?: ")
        if user_input == 'yes':
            dice_number = random.randint(1, number)
            print(f"You rolled {dice_number}")
            continue
        elif user_input == 'no':
            break
        else:
            print("Invalid selection.")
# Started by creating a user input for the dice siza and called the subroutine after that.
number = int(input('How many sides?: '))
dice_roll(number)
