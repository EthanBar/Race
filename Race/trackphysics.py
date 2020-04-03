import math


class Track:

    def __init__(self, array):
        """
        Creates a new track of a certain length.

        By default, start and end nodes a created with a height of 0
        :param length (float): How long the track should be (cannot be changed later)
        """
        if len(array) == 0:
            raise ValueError("Track cannot be zero long")
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
    def run_race(self, racers, calculations_per_unit=1):
        """
        :param racers: Array containing each racer
        :param calculations_per_unit: How many simulation iterations per unit of track
        :return:
        """

        if len(racers) == 0:
            raise ValueError("Can't run a race with no racers")

        racer_results = {}

        # Run races and record results to racer_results
        for racer in racers:
            time = self._determine_time(racer, calculations_per_unit)
            if time in racer_results.keys():
                racer_results[time].append(racer.name)
            else:
                racer_results[time] = [racer.name]

        # Iterate through race times and print results
        place = 1
        for time in sorted(racer_results):
            for racer_name in racer_results[time]:
                message = '{}. {} finished in {} seconds!'.format(place, racer_name, time)
                print(message)
            place += len(racer_results[time])
