
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
                break
        slope = (self.nodes[upper] - self.nodes[lower]) / (upper - lower)  # rise over run formula
        return slope

    def determine_time(self, racer, counts_per_second):
        """
        Calculates the time to finish this track for a specific racer
        :param racer: Which racer is attempting the race
        :param counts_per_second: How many simulation iterations per second
        :return (float): race completion time in seconds
        """
        velocity = 0
        position = 0
        time = 0
        while True:
            velocity += (racer.acceleration - self.find_slope(position)) / counts_per_second
            position += velocity / counts_per_second
            time += 1 / counts_per_second

            if position > self.length:
                return time

            if velocity <= 0:
                return "-1"  # did not finish

    # Simulate a race
    def runrace(self, racers, counts_per_second):
        """

        :param racers: Array containing each racer
        :param counts_per_second: How many simulation iterations per second
        :return:
        """

        times = {}

        for racer in racers:
            times[racer.name] = self.determine_time(racer, counts_per_second)

        for result in times:
            print("Racer " + result + " finished in " + str(times[result]) + " seconds!")
