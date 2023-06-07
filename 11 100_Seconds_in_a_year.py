# Input from user to enter the year.
year = int(input("Enter a year: "))
# This if function is to check if it's a leap year.
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap_year = True
else:
    leap_year = False
# This if function is to do the calculation for the correct year.
if leap_year:
    seconds = 366 * 24 * 60 * 60
else:
    seconds = 365 * 24 * 60 * 60
# Print function to print the result in a user friendly manner.
print("There are", seconds, "seconds in", year)
