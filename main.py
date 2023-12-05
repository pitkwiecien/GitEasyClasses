class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"Person({self.name}, {self.age}, {self.height})"


class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def __str__(self):
        return f"Animal({self.name}, {self.age}, {self.species})"


class Computer:
    def __init__(self, cost, cpu, gpu):
        self.cost = cost
        self.cpu = cpu
        self.gpu = gpu

    def __str__(self):
        return f"Computer({self.cost}, {self.cpu}, {self.gpu})"


class Monitor:
    def __init__(self, resolution, size):
        self.resolution = resolution
        self.size = size

    def __str__(self):
        return f"Computer({self.resolution}, {self.size})"


class Pen:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __str__(self):
        return f"Computer({self.color}, {self.size})"
