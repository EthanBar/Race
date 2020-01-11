import numpy


# Generates a random speed based on a normal curve
def generatespeed(mean, standard_deviation):
    speed = numpy.random.normal(mean, standard_deviation)
    while speed <= 0:  # Speeds can't be below zero!
        speed = numpy.random.normal(mean, standard_deviation)
    return speed


# Generic racer
class Racer:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Calculate speed based on racer species
    def determine_speed(self, species):
        if species == Species.DOG:
            self.speed = generatespeed(15, 10)
        elif species == Species.CAT:
            self.speed = generatespeed(25, 5)
        elif species == Species.TURTLE:
            self.speed = generatespeed(3, 3)
        elif species == Species.RABBIT:
            self.speed = generatespeed(35, 5)

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
