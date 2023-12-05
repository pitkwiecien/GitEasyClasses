class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def __str__(self):
        return f"Animal({self.name}, {self.age}, {self.species})"