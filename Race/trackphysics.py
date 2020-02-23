import math


class Track:

    def __init__(self, array):
        """
        Creates a new track of a certain length.

        By default, start and end nodes a created with a height of 0
        :param length (float): How long the track should be (cannot be changed later)
        """
        self.points = array
        self.length = len(array) - 1

    def _find_slope(self, xpos):
        """
        Calculates the slope of the track at a given point
        :param xpos: The x-position to find the slope of
        :return (float): The slope at point xpos
        """
        if xpos < 0 or xpos > self.length:
            raise ValueError("X position " + str(xpos) + " is outside the range of this track")
        lower = math.floor(xpos)
        upper = lower + 1
        print(upper)
        slope = (self.points[upper] - self.points[lower])  # rise over run formula
        return slope

    def _determine_time(self, racer, calculations_per_unit):
        """
        Calculates the time to finish this track for a specific racer
        :param racer: Which racer is attempting the race
        :param calculations_per_unit: How many simulation iterations per unit of track
        :return (float): race completion time in seconds
        """
        velocity = 0
        time = 0
        # TODO - Improve physics calculation
        for i in range(self.length):
            slope = self._find_slope(i)
            total_velocity = 0
            for _ in range(calculations_per_unit):
                velocity += (racer.acceleration - slope) / calculations_per_unit
                total_velocity += velocity
            time += 1 / total_velocity
            if velocity <= 0:
                return "-1"  # did not finish
        return round(time, 4)

    # Simulate a race
    def run_race(self, racers, calculations_per_unit):
        """

        :param racers: Array containing each racer
        :param calculations_per_unit: How many simulation iterations per unit of track
        :return:
        """

        times = {}

        for racer in racers:
            times[racer.name] = self._determine_time(racer, calculations_per_unit)

        for result in times:
            print("Racer " + result + " finished in " + str(times[result]) + " seconds!")
