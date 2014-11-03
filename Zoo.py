import requests
import Animals

database = requests.get('/database.json')


class Zoo(object):
    def __init__(self, capacity, budget):
        self.capacity = capacity
        self.budget = budget
        self.animals = []

    def see_animals(self):
        return self.animals

    def accommodate(self, animal):
        if isinstance(animal, Animals):
            self.animals.append(animal)
        else:
            print("This animal does not exist!")

    def zoo_income(self):
        for animal in self.animals:
            self.budget += 60

