import numpy
from Race import trackphysics


# Enum for species
class Species:
    DOG = 1
    CAT = 2
    TURTLE = 3
    RABBIT = 4


animals = {
    Species.DOG: [15, 10],
    Species.CAT: [25, 5],
    Species.TURTLE: [3, 3],
    Species.RABBIT: [35, 5]
}


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

        species_stats = animals[species]
        self.acceleration = generate_random_normal(species_stats[0], species_stats[1])


