class Pet:
    def __init__(self, name, species, age, adopted=False):
        self.name = name
        self.species = species
        self.age = age
        self.adopted = adopted

    def display_info(self):
        print(f"{self.name} is a {self.age}-year-old {self.species}. Adopted: {self.adopted}")
