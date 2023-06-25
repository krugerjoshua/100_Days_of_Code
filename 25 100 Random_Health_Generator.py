# Importing the random library
import random
# Added a function to roll a random dice number
def roll_dice(size):
    return random.randint(1, size)
# Function to generate the healt with the 6 dice and 8 dice.
def generate_health_stats():
    six_sided_result = roll_dice(6)
    eight_sided_result = roll_dice(8)
    health_stats = six_sided_result * eight_sided_result
    return health_stats
# Added a loop for the user interface.
while True:
    health_stats = generate_health_stats()
    name = input("Name Your Warrior: ")
    print("Character's health stats:", health_stats)
    user_input = input("Would you like to generate health stats for another character? (y/n)")
    if user_input.lower() != "y":
        break
