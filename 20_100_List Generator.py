print("List Generator")
# User inputs the desired values.
start = int(input("Start at: "))
end = int(input("End before: "))
increment = int(input("Increment between values: "))
# For loops runs the range and prints the output.
for i in range(start, end, increment):
    print(i)
