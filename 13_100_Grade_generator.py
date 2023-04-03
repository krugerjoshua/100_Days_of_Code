print("Welcome to the Grade Generator.")
subject = input("Please enter the subject: ")
total_mark = int(input("Enter the total mark of the test: "))
user_mark = int(input("Enter the Mark you got: "))
percentage = user_mark / total_mark * 100
percentage = round(percentage, 2)

if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
else:
    grade = 'U'

print(f"For {subject} you had {user_mark} out of {total_mark} and for that your percentage is {percentage}")
print(f"Your Grade is: {grade}")
