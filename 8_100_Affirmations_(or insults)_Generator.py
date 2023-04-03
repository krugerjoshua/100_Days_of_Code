print("Custom Affirmations Generator")
# call the generate_affirmation function
print("What is your name?")
name = input(":")
print("Enter the day of the week below")
day = input(":")
day = day.lower()
# define a list of affirmations
affirmations = {
    "Monday": f"You are worthy of love and respect, {name}.",
    "Tuesday": f"You are capable of achieving your goals, {name}.",
    "Wednesday": f"You are strong and resilient, {name}.",
    "Thursday": f"You are deserving of happiness and success, {name}.",
    "Friday": f"You are valuable and unique, {name}.",
    "Saturday": f"You are worthy of support and encouragement, {name}.",
    "Sunday": f"You are capable of making a positive difference, {name}."
}
# if functions to check the day of the week the user has entered
if day == "monday":
    result = affirmations.get("Monday")
elif day == "tuesday":
    result = affirmations.get("Tuesday")
elif day == "wednesday":
    result = affirmations.get("Wednesday")
elif day == "thursday":
    result = affirmations.get("Thursday")
elif day == "friday":
    result = affirmations.get("Friday")
elif day == "saturday":
    result = affirmations.get("Saturday")
elif day == "sunday":
    result = affirmations.get("Sunday")
else:
    print("Sorry wrong input. Please retry.")
# print the result
print(result) # -> "You are capable of achieving your goals, Jane." (assuming it's Tuesday)
