import unittest
import numpy
from Race import animals
from unittest.mock import patch


class Tests(unittest.TestCase):

    @patch('Race.animals.generate_random_normal', return_value=5)
    def test_animal_initialization(self, mock_normal):
        animal = animals.Racer("Joe", "Dog")
        self.assertEqual(animal.name, "Joe")
        self.assertEqual(animal.acceleration, 5)

    @patch('numpy.random.normal', return_value=3)
    def test_random_normal(self, mock_normal):
        self.assertEqual(animals.generate_random_normal(1, 1), 3)

    def test_normal_distribution(self):
        self.assertTrue(animals.generate_random_normal(1, 10) > 0)
        with self.assertRaises(ValueError):
            animals.generate_random_normal(-1, 1)
        with self.assertRaises(ValueError):
            animals.generate_random_normal(1, -1)

    def test_enum_structure(self):
        self.assertEqual(len(animals.Species), len(animals.animalStats))

    def test_animal_generation(self):
        animal = animals.Racer("Bob", animals.Species(1).name)
        self.assertEqual(animal.name, "Bob")
        self.assertTrue(animal.acceleration > 0)

    def test_incorrect_species_name(self):
        with self.assertRaises(ValueError):
            animals.Racer("Bob", "Sharknoceros")

    @patch('numpy.random.normal', side_effect=[-1, 1])
    def test_negative_random(self, mock_normal):
        self.assertEqual(animals.generate_random_normal(1, 1), 1)
        self.assertEqual(mock_normal._mock_call_count, 2)


if __name__ == '__main__':
    unittest.main()
