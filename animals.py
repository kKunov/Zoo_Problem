class Animals:
    animals_name = {}

    def __init__(self, name, age, species, gender, weight):
        self.age = age
        self.species = species
        self.gender = gender
        self.weight = weight
        self.get_name(name)

    def get_name(self, name):
        if self.species in animals_name:
            animals_name[self.species] = name
            self.name = name
        else:
            if name not in animals_name[self.species]:
                animals_name[self.species].append(name)
                self.name = name
            else:
                return ValueError

    def grow(self):
        self.age += 1
        self.weight += 3
        is_it_die(self):
