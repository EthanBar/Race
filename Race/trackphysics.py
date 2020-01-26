
class Track:

    # Initialize a new track
    def __init__(self, length):
        self.nodes = {0: 0, length: 0}
        self.length = length  # how long is the track

    # Add a new node with a certain height
    def add_node(self, xpos, height):
        if xpos < 0 or xpos > self.length:
            raise ValueError("X position " + xpos + " is outside the range of this track")

    # Simulate a race
    def runrace(self, animal1, animal2):
        # Calculate individual times
        racetime1 = (self.length / animal1.speed) + (self.angle * animal1.weight)
        racetime2 = (self.length / animal2.speed) + (self.angle * animal2.weight)

        # Compare times for a winner
        if racetime1 < racetime2:
            print(animal1.name + " wins!")
        else:
            print(animal2.name + " wins!")

