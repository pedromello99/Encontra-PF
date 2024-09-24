import unittest
from numerario_analysis import find_combinations

class TestNumerarioAnalysis(unittest.TestCase):
    def test_find_combinations(self):
        X = [70,50,22,10]
        Y = 80
        result = find_combinations(X, Y)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()