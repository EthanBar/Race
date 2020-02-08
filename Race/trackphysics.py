import math


class Track:

    def __init__(self, array):
        """
        Creates a new track of a certain length.

        By default, start and end nodes a created with a height of 0
        :param length (float): How long the track should be (cannot be changed later)
        """
        self.points = array
        self.length = len(array)


    def add_node(self, xpos, height):
        """
        Adds a new node to the track
        :param xpos: The x-position being modified
        :param height: The height to set the x-position to
        :return:
        """
        if xpos < 0 or xpos > self.length:
            raise ValueError("X position " + str(xpos) + " is outside the range of this track")
        self.points[xpos] = height

    def find_slope(self, xpos):
        """
        Calculates the slope of the track at a given point
        :param xpos: The x-position to find the slope of
        :return (float): The slope at point xpos
        """
        if xpos < 0 or xpos > self.length:
            raise ValueError("X position " + str(xpos) + " is outside the range of this track")
        lower = int(math.trunc(xpos))
        upper = lower + 1
        print(upper)
        slope = (self.points[upper] - self.points[lower])  # rise over run formula
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
    def run_race(self, racers, counts_per_second):
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
