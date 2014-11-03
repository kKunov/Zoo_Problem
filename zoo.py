import requests
import animals

database = requests.get('/database.json')


class Zoo(object):

    def __init__(self, capacity, budget):
        self.capacity = capacity
        self.budget = budget
        self.animals = []

    def see_animals(self):
        return self.animals

    def accommodate(self, animal):
        if isinstance(animal, animals):
            if len(self.animals) < self.capacity:
                self.animals.append(animal)
            else:
                print("Capacity is full. Animal was not added")
        else:
            print("This animal does not exist!")

    def zoo_daily_balance(self):
        for animal in self.animals:
            self.budget += 60
            if database.json()['animals'][animal.spieces]['food_type'] == "carnivore":
                self.budget -= 4
            elif database.json()['animals'][animal.spieces]['food_type'] == "herbivore":
                self.budget -= 2



