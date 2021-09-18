import unittest
from solver import Puzzle
import helpers

class HelperTests(unittest.TestCase):

    def test_swap_works_properly(self):
        self.assertEqual(helpers.swap(
            [6, 13, 7, 10, 8, 9, 12, 11, 15, 2, 16, 5, 14, 3, 1, 4], 3, 10),
            [6, 13, 7, 16, 8, 9, 12, 11, 15, 2, 10, 5, 14, 3, 1, 4]
        )

    def test_correct_16_index_found(self):
        self.assertEqual(helpers.find_16([6, 13, 7, 16, 8, 9, 12, 11, 15, 2, 10, 5, 14, 3, 1, 4]), 3)

    def test_puzzle_string_is_created_properly(self):
        self.assertEqual(helpers.puzzle_to_string(
            [6, 13, 7, 16, 8, 9, 12, 11, 15, 2, 10, 5, 14, 3, 1, 4]),
            "6d7x89cbf2a5e314"
        )

    def test_manhattan_distance_is_calculated_properly(self):
        self.assertEqual(helpers.manhattan_distance(
            [6, 13, 7, 16, 8, 9, 12, 11, 15, 2, 10, 5, 14, 3, 1, 4]),
            39
        )

    def test_complete_puzzle_is_completed(self):
        self.assertEqual(helpers.is_complete([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), True)

    def test_uncompleted_puzzle_is_not_completed(self):
        self.assertEqual(helpers.is_complete([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 15]), False)

    def test_correct_successors_are_returned_in_correct_order1(self):
        self.assertEqual(helpers.get_successors(
            [6, 13, 7, 16, 8, 9, 12, 11, 15, 2, 10, 5, 14, 3, 1, 4]),
            [
                [6, 13, 7, 11, 8, 9, 12, 16, 15, 2, 10, 5, 14, 3, 1, 4],
                [6, 13, 16, 7, 8, 9, 12, 11, 15, 2, 10, 5, 14, 3, 1, 4],
            ]
        )

    def test_correct_successors_are_returned_in_correct_order2(self):
        self.assertEqual(helpers.get_successors(
            [6, 13, 7, 11, 8, 9, 12, 16, 15, 2, 10, 5, 14, 3, 1, 4]),
            [
                [6, 13, 7, 11, 8, 9, 12, 5, 15, 2, 10, 16, 14, 3, 1, 4],
                [6, 13, 7, 16, 8, 9, 12, 11, 15, 2, 10, 5, 14, 3, 1, 4],
                [6, 13, 7, 11, 8, 9, 16, 12, 15, 2, 10, 5, 14, 3, 1, 4],
            ]
        )

    def test_correct_successors_are_returned_in_correct_order2(self):
        self.assertEqual(helpers.get_successors(
            [6, 13, 7, 11, 8, 9, 16, 12, 15, 2, 10, 5, 14, 3, 1, 4]),
            [
                [6, 13, 16, 11, 8, 9, 7, 12, 15, 2, 10, 5, 14, 3, 1, 4],
                [6, 13, 7, 11, 8, 9, 10, 12, 15, 2, 16, 5, 14, 3, 1, 4],
                [6, 13, 7, 11, 8, 9, 12, 16, 15, 2, 10, 5, 14, 3, 1, 4],
                [6, 13, 7, 11, 8, 16, 9, 12, 15, 2, 10, 5, 14, 3, 1, 4],
            ]
        )

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

    #def test_puzzle_cannot_be_solved_if_there_are_no_solution(self):
    #    puzzle = Puzzle([16, 14, 8, 12, 10, 11, 9, 13, 2, 6, 4, 1, 3, 7, 5, 15])
    #    self.assertEqual(puzzle.solve(), "Unsolvable!")

    #def test_puzzle_solving_works(self):
    #    puzzle = Puzzle([15, 14, 8, 12, 10, 11, 9, 13, 2, 6, 4, 1, 3, 7, 5, 16])
    #    self.assertEqual(puzzle.solve(), [51, [15, 14, 8, 12, 10, 11, 9, 13, 2, 6, 4, 1, 3, 7, 5, 16]])

if __name__ == "__main__":
    unittest.main()