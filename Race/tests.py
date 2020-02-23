import unittest
import animals


class Tests(unittest.TestCase):

    # Returns True or False.
    def test_animal_species_enum(self):
        species = animals.Racer.convert_animal_to_enum("Dog")
        self.assertEqual(species, animals.Species.DOG)

    def test_normal_distribution(self):
        self.assertTrue(animals.generate_random_normal(1, 10) > 0)

    def test_enum_structure(self):
        self.assertEqual(len(animals.Species), len(animals.animalStats))


if __name__ == '__main__':
    unittest.main()
