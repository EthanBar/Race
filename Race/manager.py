class RaceTrack:

    # Initialize a new track
    def __init__(self, length, angle):
        self.length = length # how long is the track
        self.angle = angle # how steep is the track (-90 - 90 degrees)

    # Simulate a race
    def runrace(self, animal1, animal2):
        # Calculate individual times
        racetime1 = (self.length / animal1.speed) + (self.angle * animal1.weight)
        racetime2 = (self.length/ animal2.speed) + (self.angle * animal2.weight)

        # Compare times for a winner
        if racetime1 < racetime2:
            print(animal1.name + " wins!")
        else:
            print(animal2.name + " wins!")
