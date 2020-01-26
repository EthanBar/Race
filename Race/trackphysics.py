
class Track:

    # Initialize a new track
    def __init__(self, length):
        self.nodes = {0: 0, length: 0}
        self.points = [0, length]
        self.length = length  # how long is the track

    # Add a new node with a certain height
    def add_node(self, xpos, height):
        if xpos < 0 or xpos > self.length:
            raise ValueError("X position " + str(xpos) + " is outside the range of this track")
        self.nodes[xpos] = height
        self.points.append(xpos)
        self.points.sort()

    # Returns the slope of a specific point
    def find_slope(self, xpos):
        if xpos < 0 or xpos > self.length:
            raise ValueError("X position " + str(xpos) + " is outside the range of this track")
        lower = 0
        upper = 0
        print(self.points)
        for i in range(0, len(self.points)):
            if xpos < self.points[i]:
                lower = self.points[i - 1]
                upper = self.points[i]
                print("xpos of " + str(xpos) + " found a lower of " + str(lower) + " and upper of " + str(upper))
                break
        slope = (self.nodes[upper] - self.nodes[lower]) / (upper - lower)  # rise over run formula
        return slope

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

