import unittest
from src.app import heuristic

class TestManhattanDistanceHeuristic(unittest.TestCase):
    
    def test_manhattan_distance_is_calculated_properly(self):
        self.assertEqual(heuristic.manhattan_distance(
            [6, 13, 7, 16, 8, 9, 12, 11, 15, 2, 10, 5, 14, 3, 1, 4]),
            39
        )

if __name__ == "__main__":
    unittest.main()