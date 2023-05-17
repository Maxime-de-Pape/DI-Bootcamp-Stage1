# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
#
# Other abilities of a Circle instance:
#
# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        return 2 * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


circles = [
    Circle(3),
    Circle(5),
    Circle(2)
]


sorted_circles = sorted(circles)

for circle in sorted_circles:
    print(circle)

# What You Will Learn :
# Modules
#
#
# Instructions :
# Consider this list
#
# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
# Look at this result :
# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# You have to recreate the result using a translator module.
#
#
import translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translated_words = {}

for word in french_words:
    translation = translator.translate(word, "fr", "en")  # Error 2: Incorrect function name or arguments
    translated_words[word] = translation

print(translated_words)  # Error 3: Missing closing parenthesis in print() function
