#morty2.py

class Morty(object):
    def __init__(self, universe):
        self.universe = universe

    def test_is_assigned(self):
        morty = Morty(111)
        self.assertFalse(morty.is_assigned)
