# Exercise 11 : Sandwich Orders#2
# Instructions
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Pastrami sandwich", "Pastrami sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
print("Sorry, we have run out of pastrami.")

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

print("All sandwiches are made:")
for sandwich in finished_sandwiches:
    print(sandwich)
