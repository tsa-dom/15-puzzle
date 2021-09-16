import unittest
from solver import Puzzle

class TestSolutionExistence(unittest.TestCase):

    def test_solution_is_not_found_1(self):
        puzzle = Puzzle([2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.assertEqual(puzzle.has_solution(), False)

    def test_solution_is_not_found_2(self):
        puzzle = Puzzle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 16])
        self.assertEqual(puzzle.has_solution(), False)

    def test_solution_is_not_found_3(self):
        puzzle = Puzzle([1, 2, 3, 4, 5, 6, 10, 8, 9, 16, 7, 11, 13, 14, 15, 12])
        self.assertEqual(puzzle.has_solution(), False)

    def test_solution_is_not_found_4(self):
        puzzle = Puzzle([1, 2, 15, 4, 8, 6, 7, 5, 9, 10, 11, 12, 14, 13, 3, 16])
        self.assertEqual(puzzle.has_solution(), False)

    def test_solution_found_1(self):
        puzzle = Puzzle([1, 2, 3, 4, 5, 6, 7, 16, 9, 10, 11, 8, 13, 14, 15, 12])
        self.assertEqual(puzzle.has_solution(), True)

    def test_solution_found_2(self):
        puzzle = Puzzle([6, 13, 7, 10, 8, 9, 12, 11, 15, 2, 16, 5, 14, 3, 1, 4])
        self.assertEqual(puzzle.has_solution(), True)

if __name__ == "__main__":
    unittest.main()