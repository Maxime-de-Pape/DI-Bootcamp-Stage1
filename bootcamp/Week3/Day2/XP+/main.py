#Exercise 1 : Family
#Instructions
#Create a class called Family and implement the following attributes:

#members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
#last_name : (string)
#Initial members data:

#[
    #    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    #   {'name':'Sarah','age':32,'gender':'Female','is_child':False}
#]


#2. Implement the following methods: * born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family. * is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not. * family_presentation: a method that prints the family’s last name and all the members’ first name.

class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        child = {'name': kwargs.get('name', ''), 'age': kwargs.get('age', 0), 'gender': kwargs.get('gender', ''), 'is_child': True}
        self.members.append(child)
        print(f"Congratulations! {child['name']} was born in the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        for member in self.members:
            print(f"Member: {member['name']}")


members_data = [{'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False}, {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}]

family = Family('Smith', members_data)

family.born(name='John', age=1, gender='Male')
print(family.is_18('John'))
family.family_presentation()


#Exercise 2 : TheIncredibles Family
#Instructions
#Create a class called TheIncredibles. This class should inherit from the Family class:
#This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.

#Initial members data:

[
    #   {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    #   {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]


#2. Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


#3. Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.


#4. Call the incredible_presentation method.


#5. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.


#6. Call the incredible_presentation method again.

class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        child = {'name': kwargs.get('name', ''), 'age': kwargs.get('age', 0), 'gender': kwargs.get('gender', ''), 'is_child': True}
        self.members.append(child)
        print(f"Congratulations! {child['name']} was born in the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        for member in self.members:
            print(f"Member: {member['name']}")


class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['name']} can use their power: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old!")

    def incredible_presentation(self):
        super().family_presentation()
        print("Incredible Members:")
        for member in self.members:
            if 'power' in member and 'incredible_name' in member:
                print(f"Name: {member['name']}, Power: {member['power']}, Incredible Name: {member['incredible_name']}")


members_data = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

family = TheIncredibles('Incredible', members_data)
family.incredible_presentation()
family.born(name='Baby Jack', age=0, gender='Male', power='Unknown Power')
family.incredible_presentation()
