import numpy


# Generates a random number based on a normal curve
def generate_random_normal(mean, standard_deviation):
    num = numpy.random.normal(mean, standard_deviation)
    while num <= 0:  # Speed and weight can't be below zero!
        num = numpy.random.normal(mean, standard_deviation)
    return num


# Generic racer
class Racer:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.determine_speed(species)
        self.determine_weight(species)

    # Calculate speed based on racer species
    def determine_speed(self, species):
        """
        :param species:
        :return:
        """
        if species == Species.DOG:
            self.speed = generate_random_normal(15, 10)
        elif species == Species.CAT:
            self.speed = generate_random_normal(25, 5)
        elif species == Species.TURTLE:
            self.speed = generate_random_normal(3, 3)
        elif species == Species.RABBIT:
            self.speed = generate_random_normal(35, 5)

    # Calculate weight based on racer species
    def determine_weight(self, species):
        if species == Species.DOG:
            self.weight = generate_random_normal(45, 20)
        elif species == Species.CAT:
            self.weight = generate_random_normal(10, 5)
        elif species == Species.TURTLE:
            self.weight = generate_random_normal(20, 20)
        elif species == Species.RABBIT:
            self.weight = generate_random_normal(3, 1.5)


# Enum for species
class Species:
    DOG = 1
    CAT = 2
    TURTLE = 3
    RABBIT = 4


# deprecated


class Rabbit:
    speed = 10
    weight = 1

    # Initialize a new rabbit racer
    def __init__(self, racername):
        self.name = racername


class Turtle:
    speed = 2
    weight = 5

    # Initialize a new turtle racer
    def __init__(self, racername):
        self.name = racername
