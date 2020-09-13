import unittest

class FirstTestClass(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('rubiks code'.upper(), 'RUBIKS CODE')
        
    def test_lower(self):
        self.assertEqual('RUBIKS CODE'.lower(), 'rubiks code')
        
if __name__ == '__main__':
    unittest.main()