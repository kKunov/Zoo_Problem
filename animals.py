import random
import json


class Animals:
    animals_name = {}

    def __init__(self, name, age, species, gender, weight):
        self.age = age
        self.species = species
        self.gender = gender
        self.weight = weight
        self.get_name(name)
        self.dead = True

    def get_name(self, name):
        if self.species in Animals.animals_name:
            Animals.animals_name[self.species] = name
            self.name = name
        else:
            if name not in Animals.animals_name[self.species]:
                Animals.animals_name[self.species].append(name)
                self.name = name
            else:
                return ValueError

    def grow(self):
        self.age += 1
        self.weight += 3
        self.is_it_die()

    def is_it_die(self):
        file = open("species", "r")
        species_dict = json.loads(file.read())
        life_expectancy = species_dict[self.species]["life_expectancy"]
        chance_of_die = self.age / life_expectancy
        if chance_of_die <= random.random():
            self.dead = True
            print("%s is DEAD!!!" % self.name)

    def eat(self):
        file = open("species", "r")
        species_dict = json.loads(file.read())
        consumation = species_dict[self.species]["food_per_kilos"]
        return consumation
