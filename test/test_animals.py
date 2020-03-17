import unittest
from Race import animals


class Tests(unittest.TestCase):

    def test_normal_distribution(self):
        self.assertTrue(animals.generate_random_normal(1, 10) > 0)

    def test_enum_structure(self):
        self.assertEqual(len(animals.Species), len(animals.animalStats))
        # self.assertRaises()

    def test_animal_generation(self):
        animal = animals.Racer("Bob", animals.Species(1).name)
        self.assertEqual(animal.name, "Bob")
        self.assertTrue(animal.acceleration > 0)


if __name__ == '__main__':
    unittest.main()
