import io
import sys

import unittest
from Race import trackphysics, animals
from unittest.mock import patch


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
        with self.assertRaises(ValueError):
            trackphysics.Track.run_race(trackphysics.Track([0]), [], 1)

    @patch('Race.trackphysics.Track._determine_time', side_effect=[1, 2])
    def test_run_race(self, mock_track):
        racer1 = animals.Racer("Bob", "Dog")
        racer1.name = "Bob"
        racer2 = animals.Racer("Joe", "Dog")
        racer2.name = "Joe"

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput
        trackphysics.Track.run_race(trackphysics.Track([0, 0]), [racer1, racer2])
        sys.stdout = sys.__stdout__
        self.assertEqual("1. Bob finished in 1 seconds!\n2. Joe finished in 2 seconds!\n", capturedOutput.getvalue())


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
