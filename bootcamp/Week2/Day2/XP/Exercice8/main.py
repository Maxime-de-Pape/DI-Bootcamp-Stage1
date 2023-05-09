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
    if topping == 'quit': break
    print(f'We just added {topping} to your pizza')
    topping_list.append(topping)

print(f'Your toppings are: {", ".join(topping_list)}. Total price: {pizza_price + len(topping_list) * topping_price}')