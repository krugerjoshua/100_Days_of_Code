import random
import os, time
# function to genrate random dice rolls to generate health.
def roll_dice(size):
    return random.randint(1, size)
# Generating healt with random between 6 and 8.
def generate_health_stats():
    six_sided_result = roll_dice(6)
    twelve_sided_result = roll_dice(12)
    health_stats = six_sided_result * twelve_sided_result
    return health_stats
# Generate strength stats with two random numbers added together.
def generate_strength_stats():
    six_sided_result = roll_dice(6)
    twelve_sided_result = roll_dice(12)
    strength_stats = six_sided_result * twelve_sided_result
    return strength_stats
# Welcome Screen and rest of the inputs with the os.system("clear")
while True:
    print("Welcome to character builder.")
    print("Enter play to start or exit to leave the program")
    user_choice = input(": ")
    os.system("clear")
    if user_choice.lower() == "play":
        while True:
            health_stats = generate_health_stats()
            strength_stats = generate_strength_stats()
            name = input("Name Your Warrior: ")
            type = input("Character Type (Human, Elf, Wizard, Orc): ")
            os.system("clear")
            print("Character's Type: ", type)        
            print("Character's Health stats:", health_stats)
            print("Character's Strength stats:", strength_stats)
            user_input = input("Would you like to generate health stats for another character? (y/n)")
            if user_input.lower() == "y":
                os.system("clear")
                continue
            elif user_input.lower() == "n":
                print("Thanks for playing!")
                break
# to exit the program an else to handle wrong selections          
    elif user_choice.lower() == "exit":
        print('Goodbye')
        break
    else:
        print("Wrong Selection.")
        continue
