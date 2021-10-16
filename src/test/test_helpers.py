# pylint: skip-file

import unittest
from src.app import helpers


class TestInversionCount(unittest.TestCase):
    def test_inverstion_count_is_correct(self):
        self.assertEqual(helpers.inversion_count(
            [6, 13, 7, 10, 8, 9, 11, 16, 15, 2, 12, 5, 14, 3, 1, 4]
        ), 62)


class TestLinearConflict(unittest.TestCase):
    def test_there_is_linear_conflict_if_two_pieces_are_on_the_same_row1(self):
        self.assertEqual(helpers.linear_conflict(
            [1, 2, 3, 4, 5, 8, 7, 6, 9, 10, 11, 12, 13, 14, 15, 16], 5, 7
        ), True)

    def test_there_is_linear_conflict_if_two_pieces_are_on_the_same_row2(self):
        self.assertEqual(helpers.linear_conflict(
            [4, 2, 3, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 3, 0
        ), True)

    def test_there_is_linear_conflict_if_two_pieces_are_on_the_same_row3(self):
        self.assertEqual(helpers.linear_conflict(
            [1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 11, 12, 13, 14, 15, 16], 8, 9
        ), True)

    def test_there_is_linear_conflict_if_two_pieces_are_on_the_same_row4(self):
        self.assertEqual(helpers.linear_conflict(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 14, 13, 16], 12, 14
        ), True)

    def test_there_is_linear_conflict_if_two_pieces_are_on_the_same_col1(self):
        self.assertEqual(helpers.linear_conflict(
            [1, 2, 3, 4, 5, 10, 7, 8, 9, 6, 11, 12, 13, 14, 15, 16], 9, 5
        ), True)

    def test_there_is_linear_conflict_if_two_pieces_are_on_the_same_col2(self):
        self.assertEqual(helpers.linear_conflict(
            [1, 14, 3, 4, 5, 6, 7, 8, 9, 6, 11, 12, 13, 2, 15, 16], 1, 13
        ), True)

    def test_there_is_no_linear_conflict_if_two_pieces_are_not_on_the_same_row_or_col1(
            self):
        self.assertEqual(helpers.linear_conflict(
            [1, 7, 3, 4, 5, 6, 2, 8, 9, 6, 11, 12, 13, 14, 15, 16], 1, 6
        ), False)

    def test_there_is_no_linear_conflict_if_two_pieces_are_not_on_the_same_row_or_col2(
            self):
        self.assertEqual(helpers.linear_conflict(
            [1, 2, 3, 4, 5, 6, 14, 8, 9, 6, 11, 12, 13, 7, 15, 16], 6, 13
        ), False)

    def test_there_is_no_linear_conflict_if_tho_pieces_are_same(self):
        self.assertEqual(helpers.linear_conflict(
            [1, 2, 3, 4, 5, 6, 14, 8, 9, 6, 11, 12, 13, 7, 15, 16], 6, 6
        ), False)


class TestUtils(unittest.TestCase):
    def test_correct_tiles_are_swapped(self):
        self.assertEqual(helpers.swap_puzzle(
            [6, 13, 7, 10, 8, 9, 12, 11, 15, 2, 16, 5, 14, 3, 1, 4], 3, 10),
            [6, 13, 7, 16, 8, 9, 12, 11, 15, 2, 10, 5, 14, 3, 1, 4]
        )

    def test_index_of_16_is_correct(self):
        self.assertEqual(helpers.find_16(
            [6, 13, 7, 16, 8, 9, 12, 11, 15, 2, 10, 5, 14, 3, 1, 4]),
            3
        )

    def test_complete_puzzle_is_completed(self):
        self.assertEqual(helpers.is_complete(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]),
            True
        )

    def test_uncompleted_puzzle_is_not_completed(self):
        self.assertEqual(helpers.is_complete(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 15]),
            False
        )


class TestGetSuccessors(unittest.TestCase):

    def test_top_left_corner_works(self):
        self.assertEqual(helpers.get_successors(
            [16, 7, 10, 8, 2, 3, 5, 1, 14, 9, 13, 6, 11, 12, 4, 15], ""),
            [
                [2, 7, 10, 8, 16, 3, 5, 1, 14, 9, 13, 6, 11, 12, 4, 15],
                [7, 16, 10, 8, 2, 3, 5, 1, 14, 9, 13, 6, 11, 12, 4, 15]
        ]
        )

    def test_bottom_left_corner_works(self):
        self.assertEqual(helpers.get_successors(
            [2, 7, 10, 8, 14, 3, 5, 1, 11, 9, 13, 6, 16, 12, 4, 15], ""),
            [
                [2, 7, 10, 8, 14, 3, 5, 1, 16, 9, 13, 6, 11, 12, 4, 15],
                [2, 7, 10, 8, 14, 3, 5, 1, 11, 9, 13, 6, 12, 16, 4, 15]
        ]
        )

    def test_bottom_right_corner_works(self):
        self.assertEqual(helpers.get_successors(
            [2, 7, 10, 8, 14, 3, 5, 1, 11, 9, 13, 6, 12, 4, 15, 16], ""),
            [
                [2, 7, 10, 8, 14, 3, 5, 1, 11, 9, 13, 16, 12, 4, 15, 6],
                [2, 7, 10, 8, 14, 3, 5, 1, 11, 9, 13, 6, 12, 4, 16, 15]
        ]
        )

    def test_top_right_corner_works(self):
        self.assertEqual(helpers.get_successors(
            [2, 7, 10, 16, 14, 3, 5, 8, 11, 9, 13, 1, 12, 4, 15, 6], ""),
            [
                [2, 7, 10, 8, 14, 3, 5, 16, 11, 9, 13, 1, 12, 4, 15, 6],
                [2, 7, 16, 10, 14, 3, 5, 8, 11, 9, 13, 1, 12, 4, 15, 6]
        ]
        )

    def test_middle_area_works(self):
        self.assertEqual(helpers.get_successors(
            [2, 7, 10, 8, 14, 3, 16, 5, 11, 9, 13, 1, 12, 4, 15, 6], ""),
            [
                [2, 7, 16, 8, 14, 3, 10, 5, 11, 9, 13, 1, 12, 4, 15, 6],
                [2, 7, 10, 8, 14, 3, 5, 16, 11, 9, 13, 1, 12, 4, 15, 6],
                [2, 7, 10, 8, 14, 16, 3, 5, 11, 9, 13, 1, 12, 4, 15, 6],
                [2, 7, 10, 8, 14, 3, 13, 5, 11, 9, 16, 1, 12, 4, 15, 6],
        ]
        )

    def test_bottom_area_works(self):
        self.assertEqual(helpers.get_successors(
            [2, 7, 10, 8, 14, 3, 5, 1, 11, 9, 13, 6, 12, 16, 4, 15], ""),
            [
                [2, 7, 10, 8, 14, 3, 5, 1, 11, 9, 13, 6, 16, 12, 4, 15],
                [2, 7, 10, 8, 14, 3, 5, 1, 11, 16, 13, 6, 12, 9, 4, 15],
                [2, 7, 10, 8, 14, 3, 5, 1, 11, 9, 13, 6, 12, 4, 16, 15],
        ]
        )

    def test_top_area_works(self):
        self.assertEqual(helpers.get_successors(
            [2, 10, 16, 8, 14, 7, 5, 1, 11, 3, 13, 6, 12, 9, 4, 15], ""),
            [
                [2, 10, 5, 8, 14, 7, 16, 1, 11, 3, 13, 6, 12, 9, 4, 15],
                [2, 10, 8, 16, 14, 7, 5, 1, 11, 3, 13, 6, 12, 9, 4, 15],
                [2, 16, 10, 8, 14, 7, 5, 1, 11, 3, 13, 6, 12, 9, 4, 15],
        ]
        )

    def test_right_area_works(self):
        self.assertEqual(helpers.get_successors(
            [2, 10, 8, 1, 14, 7, 5, 16, 11, 3, 13, 6, 12, 9, 4, 15], ""),
            [
                [2, 10, 8, 1, 14, 7, 5, 6, 11, 3, 13, 16, 12, 9, 4, 15],
                [2, 10, 8, 16, 14, 7, 5, 1, 11, 3, 13, 6, 12, 9, 4, 15],
                [2, 10, 8, 1, 14, 7, 16, 5, 11, 3, 13, 6, 12, 9, 4, 15],
        ]
        )

    def test_left_area_works(self):
        self.assertEqual(helpers.get_successors(
            [2, 10, 8, 1, 11, 7, 5, 14, 16, 3, 13, 6, 12, 9, 4, 15], ""),
            [
                [2, 10, 8, 1, 11, 7, 5, 14, 12, 3, 13, 6, 16, 9, 4, 15],
                [2, 10, 8, 1, 16, 7, 5, 14, 11, 3, 13, 6, 12, 9, 4, 15],
                [2, 10, 8, 1, 11, 7, 5, 14, 3, 16, 13, 6, 12, 9, 4, 15],
        ]
        )


if __name__ == "__main__":
    unittest.main()
