#Exercise 1 : What Are You Learning ?
#Instructions
#Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
#Call the function, and make sure the message displays correctly.

def display_message():
    print("I am learning a lot in this course!")

display_message()

#🌟 Exercise 2: What’s Your Favorite Book ?
#Instructions
#Write a function called favorite_book() that accepts one parameter called title.
#The function should print a message, such as "One of my favorite books is <title>".
#For example: “One of my favorite books is Alice in Wonderland”
#Call the function, make sure to include a book title as an argument when calling the function.
def favorite_book(title):
    print("One of my favorite books is " + title)

favorite_book("Alice in Wonderland")


#🌟 Exercise 3 : Some Geography
#Instructions
def describe_city(city, country=""):
    if country:
        print(city + " is in " + country)
    else:
        print(city + " is in an unknown country")

describe_city("Reykjavik", "Iceland")
describe_city("Tokyo", "Japan")
describe_city("Paris")


#Exercise 4 : Random
#Instructions
#Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
#Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
import random


def compare_numbers(number):
    random_number = random.randint(1, 100)

    if number == random_number:
        print("Success! The numbers match.")
    else:
        print("Fail! The numbers don't match.")
        print("Given number:", number)
        print("Randomly generated number:", random_number)


compare_numbers(50)

#🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
#Instructions
#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
#The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
#Call the function make_shirt().

import random


def compare_numbers(number):
    random_number = random.randint(1, 100)

    if number == random_number:
        print("Success! The numbers match.")
    else:
        print("Fail! The numbers don't match.")
        print("Given number:", number)
        print("Randomly generated number:", random_number)


compare_numbers(50)

#Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
#Make a large shirt with the default message
#Make medium shirt with the default message
#Make a shirt of any size with a different message.
def make_shirt(size="large", text="I love Python"):
    print("The size of the shirt is " + size + " and the text is '" + text + "'.")

make_shirt()

make_shirt("medium")

make_shirt("small", "Hello, World!")



#🌟 Exercise 6 : Magicians …
#Instructions
#Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
#Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
#Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
#Call the function make_great().
#Call the function show_magicians() to see that the list has actually been modified.
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    for i in range(len(names)):
        names[i] += " the Great"

show_magicians(magician_names)

make_great(magician_names)

show_magicians(magician_names)


#🌟 Exercise 7 : Temperature Advice
#Instructions
#Create a function called get_random_temp().
#This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
#Test your function to make sure it generates expected results.
import random

def get_random_temp():
    return random.randint(-10, 40)

temperature = get_random_temp()
print("Random Temperature:", temperature)


#Create a function called main().
#Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
#Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
import random

def get_random_temp():
    return random.randint(-10, 40)

def main():
    temperature = get_random_temp()
    print("The temperature right now is", temperature, "degrees Celsius.")

main()


#Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
#below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
#between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
#between 16 and 23
#between 24 and 32
#between 32 and 40
import random

def get_random_temp():
    return random.randint(-10, 40)

def main():
    temperature = get_random_temp()
    print("The temperature right now is " + str(temperature) + " degrees Celsius.")

    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    if temperature >= 0 and temperature <= 16:
        print("Quite chilly! Don't forget your coat.")
    if temperature > 16 and temperature <= 23:
        print("It's a moderate temperature.")
    if temperature >= 24 and temperature <= 32:
        print("Enjoy the pleasant weather.")
    if temperature > 32 and temperature <= 40:
        print("It's hot outside. Stay hydrated.")

main()


#Change the get_random_temp() function:
#Add a parameter to the function, named ‘season’.
#Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
#Now that we’ve changed get_random_temp(), let’s change the main() function:
#Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
#Use the season as an argument when calling get_random_temp().

import random

def get_random_temp(season):
    temperature = 0
    if season == 'winter':
        temperature = random.randint(-10, 16)
    if season == 'spring':
        temperature = random.randint(5, 23)
    if season == 'summer':
        temperature = random.randint(20, 35)
    if season == 'autumn' or season == 'fall':
        temperature = random.randint(10, 24)
    return temperature

def main():
    season = input("Please enter the season (summer, autumn, winter, or spring): ")

    temperature = get_random_temp(season)
    print("The temperature right now is", temperature, "degrees Celsius.")

    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    if temperature >= 0 and temperature <= 16:
        print("Quite chilly! Don't forget your coat.")
    if temperature > 16 and temperature <= 23:
        print("It's a moderate temperature.")
    if temperature > 23 and temperature <= 32:
        print("Enjoy the pleasant weather.")
    if temperature > 32:
        print("It's hot outside. Stay hydrated.")

main()










#Bonus: Give the temperature as a floating-point number instead of an integer.
#Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
