# 🌟 Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {1, 7, 24}
my_fav_numbers.add(9)
my_fav_numbers.add(11)
my_fav_numbers.remove(11)

friend_fav_numbers = {7, 1, 78}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)

# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
#
# No
#


# 🌟 Exercise 3: List
# Instructions
# create a list called basket
basket = ["ETHEREUM", "DOT", "SOLANA", "AAVE"]

basket.remove('ETHEREUM')
basket.remove('DOT')

basket.append('BITCOIN')

basket.insert(0, 'AAVE')

count = len(basket)

basket.clear()

print(basket)


# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
seq = []
for i in range(8):
    seq.append(1.5 + i/2)
print(seq)

# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for j in range(1, 21):
    if j % 2 == 0:
        print(j)

# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for i in range(1, 21):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
name = ""
my_name = 'Maxime'
user_name = ''

while user_name != my_name:
    user_name = input('What is your name?')
    if user_name == my_name:
        print("Hello, Maxime!")
    else:
        print("Sorry, I don't know you.")


# 🌟 Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

favorite_fruits = input('What is your favorite fruit(s). Separate the fruits with a single space, eg. "apple mango cherry"\n')
favorite_fruits_list = favorite_fruits.split()
selected_fruit = input('Select any fruit: ')

if selected_fruit in favorite_fruits_list:
    print("You selected one of your favorite fruits! Bon appétit!")
else:
    print("You selected a new fruit. I hope you enjoy it.")
# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

pizza_price = 10
topping_price = 2.5
topping_list = []

while True:
    topping = input('What topping to add? (type "quit" to stop)\n')
    if topping == 'quit':
        break
    print('We just added ' + topping + ' to your pizza.')
    topping_list.append(topping)

topping_count = len(topping_list)
total_price = pizza_price + topping_count * topping_price
print('Your toppings are: ' + ', '.join(topping_list) + '. Total price: ' + str(total_price))


# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
#
# Ask a family the age of each person who wants a ticket.
#
# Store the total cost of all the family’s tickets and print it out.

num_people = int(input("How many people need tickets? "))
total_cost = 0

for i in range(num_people):
    age = int(input("Enter age of person #" + str(i + 1) + ": "))
    if age < 3:
        ticket_cost = 0
    elif age <= 12:
        ticket_cost = 10
    else:
        ticket_cost = 15

    total_cost += ticket_cost

print("The total cost of all tickets is:")
print(total_cost)






# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

if not age_input.isdigit():
    print("You entered an invalid age. Please try again.")
    continue

age = int(age_input)

if age < 16:
    print(name + " is too young to watch the movie.")
    teenagers.remove(name)
elif age >= 21:
    print(name + " is too old to watch the movie.")
    teenagers.remove(name)
else:
    i += 1

# Exercise 10 : Sandwich Orders
# Instructions
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
#
# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.


sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

print("The following sandwiches will be made:")
for sandwich in sandwich_orders:
    print(sandwich)

print("\n")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    if current_sandwich != "Pastrami sandwich":
        print(f"I made your {current_sandwich}.")

# Exercise 11 : Sandwich Orders#2
# Instructions
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Pastrami sandwich", "Pastrami sandwich",
                   "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
print("Sorry, we have run out of pastrami.")

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print("I made your " + sandwich + ".")
    finished_sandwiches.append(sandwich)

print("All sandwiches are made:")
for sandwich in finished_sandwiches:
    print(sandwich)
