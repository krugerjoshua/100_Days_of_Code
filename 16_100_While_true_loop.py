# A game where you need to fill in the mising lyrics.
print("Fill in the blank lyrics!")
count = 0
# A while loop with ifs too see if the conditions are met.
while True:
    print("Never going to ______ you up.")
    word = input()
    count += 1
    if word == 'give':
        count = count - 1
        print(f"Well done it only took {count} attempts.")
        break
    else:
        print("Nope, let's try again.")
