#Take a look at the following code and output:
#File: market.py

#macdonald = Farm("McDonald")
#macdonald.add_animal('cow',5)
#macdonald.add_animal('sheep')
#macdonald.add_animal('sheep')
#macdonald.add_animal('goat', 12)
#print(macdonald.get_info())
#Output

#McDonald's farm

#cow : 5
#sheep : 2
#goat : 12
#
#    E-I-E-I-0!
#
#
#Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

#Create a class called Farm. How should it be implemented?
#Does the Farm class need an __init__ method? If so, what parameters should it take?
#How many methods does the Farm class need?
#Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
#Test your code and make sure you get the same results as the example above.


#Expand The Farm
#Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].

#Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. The method should call the get_animal_types function to get a list of the animals.

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        farm_info = f"{self.name}'s farm\n\n"
        for animal_type, count in self.animals.items():
            farm_info += f"{animal_type} : {count}\n"
        farm_info += "\nE-I-E-I-0!"
        return farm_info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_list = ', '.join(animal_types)
        return f"{self.name}'s farm has {animal_list}."

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

animal_types = macdonald.get_animal_types()
print(f"Animal types in the farm: {animal_types}")

short_info = macdonald.get_short_info()
print(short_info)
