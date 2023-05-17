# 🌟 Exercise 1: Import
# Instructions
# In a file named func.py create a function that adds 2 number, and prints the result
# In a file namedexercise_one.py import and the function
# Hint: You can use the the following syntaxes:
#
# import module_name
#
# OR
#
# from module_name import function_name
#
# OR
#
# from module_name import function_name as fn
#
# OR
#
# import module_name as mn
#
#
# 🌟 Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

import random


def generate_random_number(user_number):
    random_number = random.randint(1, 100)

    print("Your number:", user_number)
    print("Random number:", random_number)

    if random_number == user_number:
        print("Congratulations! You guessed the same number!")
    else:
        print("Better luck next time!")



user_input = input("Enter a number between 1 and 100: ")
generate_random_number(user_input)

# 🌟 Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module
#
#
# datetime module
#

import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

# Generate a random string of length 5
random_string = generate_random_string(5)
print("Random String:", random_string)

#
#
# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

import datetime

def display_current_date():
    current_date = datetime.date.today()
    print("Current Date:", current_date)

# Call the function to display the current date
display_current_date()




#
# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).
import datetime

def display_time_left_until_january1st():
    today = datetime.date.today()
    january1st = datetime.date(today.year + 1, 1, 1)
    time_left = january1st - today
    hours_left = datetime.datetime.combine(january1st, datetime.time.min) - datetime.datetime.now()

    print(f"The 1st of January is in {time_left.days} days and {hours_left}")

# Call the function to display the amount of time left until January 1st
display_time_left_until_january1st()

#
# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.
import datetime

def calculate_minutes_lived(birthdate):
    current_datetime = datetime.datetime.now()
    time_lived = current_datetime - birthdate
    minutes_lived = int(time_lived.total_seconds() / 60)

    print(f"Maxime has lived approximately {minutes_lived} minutes, i hope he will last at least double that amount.")

# Example usage
birthdate = datetime.datetime(1997, 7, 27)  # Replace with the actual birthdate
calculate_minutes_lived(birthdate)

#
# Exercise 7 : Upcoming Holiday
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.
#
import datetime

def display_upcoming_holiday():
    today = datetime.date.today()
    upcoming_holiday_date = datetime.date(today.year, 12, 25)  #Christmas yeey

    time_left = upcoming_holiday_date - today
    hours_left = datetime.datetime.combine(upcoming_holiday_date, datetime.time.min) - datetime.datetime.now()

    print(f"The next holiday is {upcoming_holiday_date.strftime('%B %d')}.")
    print(f"It is in {time_left.days} days and {hours_left} hours. Oh Oh Oh...")

display_upcoming_holiday()

# Exercise 8 : How Old Are You On Jupiter?
# Instructions
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.
#
#
def calculate_age_on_planets(age_in_seconds):
    earth_year_seconds = 31557600
    orbital_periods = {
        'Earth': 1.0,
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132
    }

    earth_years = age_in_seconds / earth_year_seconds

    age_on_planets = {}
    for planet, orbital_period in orbital_periods.items():
        age_on_planets[planet] = round(earth_years // orbital_period, 2)

    return age_on_planets


age_in_seconds = 1000000000
age_on_planets = calculate_age_on_planets(age_in_seconds)
print(f"Age on different planets: {age_on_planets}")


# Exercise 9 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.
import random
from faker import Faker

users = []

def add_user():
    fake = Faker()

    name = fake.name()
    address = fake.address()
    language_code = random.choice(['en', 'fr', 'es', 'de'])

    user = {
        'name': name,
        'address': address,
        'language_code': language_code
    }

    users.append(user)

add_user()
add_user()
add_user()

print(users)
