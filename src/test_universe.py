#test_universe.py

#rick_tests1.py

import unittest
from rick1 import Rick

class RickTests(unittest.TestCase):
    def test_universe(self):
        rick = Rick(111)
        self.assertEqual(rick.universe, 111)
        

    #morty_tests1.py

from morty1 import Morty

class MortyTests(unittest.TestCase):
    def test_universe(self):
        morty = Morty(111)
        self.assertEqual(morty.universe, 111)
        
if __name__ == '__main__':
    unittest.main()