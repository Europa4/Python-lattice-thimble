import numpy as np
import unittest
import os
from lattice import Lattice


class MyTestCase(unittest.TestCase):

    def test_blank_save_load(self):
        default_lattice = Lattice()
        default_lattice.save_to_file("tmp")
        loaded_lattice = Lattice("tmp")
        os.remove("tmp.json")
        self.assertEqual(default_lattice, loaded_lattice)

    def test_positive_save_load(self):
        default_lattice = Lattice()
        default_lattice.number_of_time_points = 10
        default_lattice.number_of_spacial_points = np.array([1, 0, 0])

        default_lattice.save_to_file("tmp")
        loaded_lattice = Lattice("tmp")
        os.remove("tmp.json")
        self.assertEqual(default_lattice, loaded_lattice)


if __name__ == '__main__':
    unittest.main()
