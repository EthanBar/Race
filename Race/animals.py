import numpy
from Race import trackphysics

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
            self.acceleration = generate_random_normal(15, 10)
        elif species == Species.CAT:
            self.acceleration = generate_random_normal(25, 5)
        elif species == Species.TURTLE:
            self.acceleration = generate_random_normal(3, 3)
        elif species == Species.RABBIT:
            self.acceleration = generate_random_normal(35, 5)

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
