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
