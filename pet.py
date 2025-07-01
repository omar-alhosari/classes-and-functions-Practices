class Pet:
    def __init__(self, name, species, age, adopted=False):
        self.name = name
        self.species = species
        self.age = age
        self.adopted = adopted

    def display_info(self):
        print(f"{self.name} is a {self.age}-year-old {self.species}. Adopted: {self.adopted}")
    def mark_adopted(self):
        self.adopted = True

    def birthday(self):
        self.age += 1
    def rename(self, new_name):
        self.name = new_name
shelter_pets = [
    Pet("Max", "dog", 4, adopted=True),
    Pet("Luna", "cat", 2),
    Pet("Coco", "rabbit", 1),
    Pet("Buddy", "dog", 3, adopted=True),
    Pet("Milo", "cat", 5)
]
def find_available_pets(pet_list):
    return [pet for pet in pet_list if not pet.adopted]

available_pets = find_available_pets(shelter_pets)
for pet in available_pets:
    pet.display_info()
