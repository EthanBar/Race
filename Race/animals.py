import numpy


class Species:
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
    Species.DOG: (15, 10),
    Species.CAT: (25, 5),
    Species.TURTLE: (3, 3),
    Species.RABBIT: (35, 5),
    Species.ELEPHANT: (25, 3)
}


# For converting user input into enum
animalNames = {
    Species.DOG: "Dog",
    Species.CAT: "Cat",
    Species.TURTLE: "Turtle",
    Species.RABBIT: "Rabbit",
    Species.ELEPHANT: "Elephant"
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
        self.species = self.convert_animal_to_enum(species)
        species_stats = animalStats[self.species]
        self.mean_speed = species_stats[0]
        self.speed_standard_deviation = species_stats[1]
        self.acceleration = generate_random_normal(self.mean_speed, self.speed_standard_deviation)

    @staticmethod
    def convert_animal_to_enum(species):
        for animal, animalName in animalNames.items():
            if species == animalName:
                return animal
        raise ValueError('{} is not a valid animal name'.format(species))
