import json
from info.models import Animal, Family

def load_data():
    with open('data.json') as file:
        data = json.load(file)

    for family_data in data['families']:
        family = Family.objects.create(name=family_data['name'])

    for animal_data in data['animals']:
        animal = Animal.objects.create(
            name=animal_data['name'],
            legs=animal_data['legs'],
            weight=animal_data['weight'],
            height=animal_data['height'],
            speed=animal_data['speed'],
            family_id=animal_data['family']
        )

load_data()
