import unittest
from Race import trackphysics


class Tests(unittest.TestCase):

    def test_length(self):
        track = trackphysics.Track([0, 0, 0, 0, 0])
        self.assertEqual(track.length, 4)


if __name__ == '__main__':
    unittest.main()
