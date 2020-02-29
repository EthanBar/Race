import numpy
from enum import Enum


class Species(Enum):
    """
    Enum for referencing species
    """
    DOG = 1
    CAT = 2
    TURTLE = 3
    RABBIT = 4
    ELEPHANT = 5


# Contains animals unique statistics
# [mean, standard deviation]
animalStats = {
    Species.DOG: (15, 2),
    Species.CAT: (25, 1),
    Species.TURTLE: (3, 1),
    Species.RABBIT: (35, 3),
    Species.ELEPHANT: (25, 3)
}


def generate_random_normal(mean, standard_deviation):
    """
    Generates a random number based on a normal curve
    :param mean: average number if many numbers were generated
    :param standard_deviation: how far the average value strays from the mean
    :return: random float point
    """
    num = numpy.random.normal(mean, standard_deviation)
    while num <= 0:  # Speed and weight can't be below zero!
        num = numpy.random.normal(mean, standard_deviation)
    return num


class Racer:

    def __init__(self, name, species):
        """
        Creates a new generic racer
        :param name: string name of racer
        :param species: string used to find animal species
        """
        self.name = name
        self.species = Species[species.upper()]
        self.mean_speed, self.speed_standard_deviation = animalStats[self.species]
        self.acceleration = generate_random_normal(self.mean_speed, self.speed_standard_deviation)

