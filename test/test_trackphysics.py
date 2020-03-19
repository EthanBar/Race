import unittest
from Race import trackphysics, animals


class Tests(unittest.TestCase):

    def test_length(self):
        track = trackphysics.Track([0, 0, 0, 0, 0])
        self.assertEqual(track.length, 4)

    def test_slope(self):
        track = trackphysics.Track
        track.points = [0, 1]
        track.length = 1
        self.assertEqual(trackphysics.Track._find_slope(track, 0.5), 1)

    def test_empty_racers(self):
        try:
            trackphysics.Track.run_race(trackphysics.Track([]), [], 1)
        except:
            self.fail("Empty array of racers caused track to raise exception")

    def test_determine_time(self):
        track = trackphysics.Track
        track.points = [0, 1]
        track.length = 1
        animal = animals.Racer
        animal.acceleration = 0.5
        self.assertEqual(trackphysics.Track._determine_time(track, animal, 1), 5)



if __name__ == '__main__':
    unittest.main()
