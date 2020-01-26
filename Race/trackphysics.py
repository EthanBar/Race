
class Track:

    def __init__(self, length):
        """
        Creates a new track of a certain length.

        By default, start and end nodes a created with a height of 0
        :param length (float): How long the track should be (cannot be changed later)
        """
        self.nodes = {0: 0, length: 0}
        self.points = [0, length]
        self.length = length

    def add_node(self, xpos, height):
        """
        Adds a new node to the track
        :param xpos: The x-position being modified
        :param height: The height to set the x-position to
        :return:
        """
        if xpos < 0 or xpos > self.length:
            raise ValueError("X position " + str(xpos) + " is outside the range of this track")
        self.nodes[xpos] = height
        self.points.append(xpos)
        self.points.sort()

    def find_slope(self, xpos):
        """
        Calculates the slope of the track at a given point
        :param xpos: The x-position to find the slope of
        :return (float): The slope at point xpos
        """
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

