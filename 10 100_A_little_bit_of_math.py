# This section lets the user enter the bill amount, number of people and tip percentage.
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("Enter the tip percentage: "))

# This section is where all the correct calculations is done.
tip_division = tip / 100 * myBill
tip_amount = tip_division + myBill
answer = tip_amount / numberOfPeople
answer = round(answer, 2)

# After the calculations the total is displayed in a friendly matter.
print("You all owe R",answer)
