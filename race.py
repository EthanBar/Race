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


class RaceTrack:

    # Initialize a new track
    def __init__(self, length, angle):
        self.length = length # how long is the track
        self.angle = angle # how steep is the track (-90 - 90 degrees)

    # Simulate a race
    def runrace(self, animal1, animal2):
        # Calculate individual times
        racetime1 = (animal1.speed * self.length) + (self.angle * animal1.weight)
        racetime2 = (animal2.speed * self.length) + (self.angle * animal2.weight)

        # Compare times for a winner
        if racetime1 < racetime2:
            print(animal1.name + " wins!")
        else:
            print(animal2.name + " wins!")


# Tests
turtle = Turtle("Jared")
rabbit = Rabbit("Jack")

track1 = RaceTrack(10, -50)
track2 = RaceTrack(10, 50)

track1.runrace(turtle, rabbit)
track2.runrace(turtle, rabbit)
