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

        results = trackphysics.Track.run_race(trackphysics.Track([0, 0]), [racer1, racer2])
        self.assertEqual({1: ['Bob'], 2: ['Joe']}, results)

    @patch('Race.trackphysics.Track._find_slope', side_effect=[1])
    def test_determine_time_mock_slope(self, mock_slope):
        track = trackphysics.Track([0, 1])
        track.points = [0, 0.5]
        track.length = 1

        racer1 = animals.Racer("Bob", "Dog")
        racer1.acceleration = 2

        self.assertEqual(trackphysics.Track._determine_time(track, racer1, 2), 66.667)

    def test_empty_track(self):
        with self.assertRaises(ValueError):
            trackphysics.Track([])

    def test_determine_time(self):
        track = trackphysics.Track([0, 1])
        track.points = [0, 1]
        track.length = 1
        animal = animals.Racer("Bob", "Dog")
        animal.acceleration = 5
        self.assertEqual(trackphysics.Track._determine_time(track, animal, 1), 25)

    def test_length_upper(self):
        track = trackphysics.Track([0, 1])
        with self.assertRaises(ValueError):
            track._find_slope(2)

    def test_length_lower(self):
        track = trackphysics.Track([0, 1])
        with self.assertRaises(ValueError):
            track._find_slope(-1)

    def test_duplicate_racer(self):
        track = trackphysics.Track([0, 1])
        track.points = [0, 1]
        track.length = 1
        animal1 = animals.Racer("Bob", "Dog")
        animal2 = animals.Racer("Joe", "Dog")
        animal1.acceleration = 5
        animal2.acceleration = 5
        trackphysics.Track.run_race(track, [animal1, animal2])

    def test_failure_to_finish(self):
        track = trackphysics.Track([0, 10, 100, -100, 0])
        track.points = [0, 10, 100, -100, 0]
        track.length = 4
        animal = animals.Racer("Bob", "Dog")
        animal.acceleration = 1
        self.assertEqual(trackphysics.Track._determine_time(track, animal, 5), -1)


class IntegrationTests(unittest.TestCase):

    def test_track_physics(self):
        # setting up racers
        racer1 = animals.Racer("Bob", "Dog")
        racer1.name = "Bob"
        racer1.acceleration = 1
        racer2 = animals.Racer("Joe", "Dog")
        racer2.name = "Joe"
        racer2.acceleration = 3

        track = trackphysics.Track([0, 2, 5, 0])
        results = track.run_race([racer1, racer2], 5)

        self.assertEqual(results, {-1: ['Bob'], 56.782: ['Joe']})


if __name__ == '__main__':
    unittest.main()
