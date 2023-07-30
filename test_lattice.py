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


if __name__ == '__main__':
    unittest.main()
