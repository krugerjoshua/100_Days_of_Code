# Start of a fun multiplication testing game.
print("Multiplication Knowledge")

# Created 2 variables for the users number and one to keep tyrack of score.
number = int(input("Chose the number for multiplication: "))
score = 0

# Starting with a for loop to run through each multiplication.
for i in range(1, 11):
    correct_answer = i * number
    answer = int(input(f"{i} X {number} = "))
    if answer == correct_answer:
        print("That's correct!!")
        score += 1
        continue
    else:
        print("Sorry that's not it")
        score = score
        continue

# Print the score the user achieved
print(f"Congrats you are done and scored {score} out of 10")
