from src.example_package.example import add_one 

import unittest

class TestExample(unittest.TestCase):
    def test(self):
        self.assertEqual(2, add_one(1))
        
        
if __name__ == "__main__":
    unittest.main()