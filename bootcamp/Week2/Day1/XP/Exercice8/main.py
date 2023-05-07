predefined_name = "Maxime"  # a predefined name to compare with

user_name = input("What is your name? ")  # ask user for their name

if user_name == predefined_name:
    print("Are you my clone?")  # if user's name matches the predefined name
else:
    print("Oh hello " + user_name + "! Wassup?")  # if user's name doesn't match the predefined name
