import unittest
from Race import trackphysics


class Tests(unittest.TestCase):

    def test_length(self):
        track = trackphysics.Track([0, 0, 0, 0, 0])
        self.assertEqual(track.length, 4)

    def test_slope(self):
        track = trackphysics.Track
        track.points = [0, 1]
        track.length = 1
        self.assertEqual(trackphysics.Track._find_slope(track, 0.5), 1)


if __name__ == '__main__':
    unittest.main()
