def get_generation(birth_year):
    # Map the birth year to the appropriate generation
    if birth_year < 1965:
        return "Silent"
    elif birth_year >= 1965 and birth_year < 1980:
        return "Baby Boomer"
    elif birth_year >= 1980 and birth_year < 1995:
        return "Generation X"
    elif birth_year >= 1995 and birth_year < 2010:
        return "Millennial"
    else:
        return "Generation Z"

# Ask the user for their birth year
birth_year = int(input("Please enter your birth year: "))

# Get the user's generation and print it
generation = get_generation(birth_year)
print(f"Based on your birth year of {birth_year}, you are a part of the {generation} generation.")
