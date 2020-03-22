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
        trackphysics.Track.run_race(trackphysics.Track([0]), [], 1)

    def test_empty_track(self):
        with self.assertRaises(ValueError):
            trackphysics.Track([])

    def test_determine_time(self):
        track = trackphysics.Track([0, 1])
        track.points = [0, 1]
        track.length = 1
        animal = animals.Racer("Bob", "Dog")
        animal.acceleration = 5
        self.assertEqual(trackphysics.Track._determine_time(track, animal, 1), 0.25)

    def test_length_extremes(self):
        track = trackphysics.Track([0, 1])
        with self.assertRaises(ValueError):
            track._find_slope(-1)
        with self.assertRaises(ValueError):
            track._find_slope(2)


if __name__ == '__main__':
    unittest.main()
