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
    :param mean: average number if many numbers were generated, should be positive
    :param standard_deviation: how far the average value strays from the mean, should be positive
    :return: random float point
    """
    if mean < 0 or standard_deviation < 0:
        raise ValueError("Cannot generate acceleration from negative mean or standard deviation")
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
        if species.upper() not in Species.__members__:
            raise ValueError("Animal species {} not found in implemented species".format(species))
        self.species = Species[species.upper()]
        self.mean_speed, self.speed_standard_deviation = animalStats[self.species]
        self.acceleration = generate_random_normal(self.mean_speed, self.speed_standard_deviation)

