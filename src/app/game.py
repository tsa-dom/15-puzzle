"""
Game module
"""

from src.app import algorithm # pylint: disable=import-error
from src.app import helpers # pylint: disable=import-error

class Puzzle:
    """
    Puzzle object
    """

    def __init__(self, puzzle, heuristic):
        """ A new puzzle initialization function
        Args:
            puzzle [int]: desired puzzle initial state
        """
        test = {1, 2, 3 ,4 ,5 ,6 ,7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
        if len(puzzle) != 16:
            raise Exception("Invalid puzzle")
        for piece in puzzle:
            if piece not in test:
                raise Exception("Invalid puzzle")
            test.remove(piece)

        self.puzzle = puzzle
        self.heuristic = heuristic

    def change_heuristic(self, heuristic):
        """ Changes heuristic of the existing puzzle
        Args:
            heuristic string: heuristic name
        """
        self.heuristic = heuristic

    def has_solution(self):
        """ Checks if the puzzle has a solution
        Returns:
            bool: true if the solution exist and false if not
        """

        even = None
        for i in range(16):
            if self.puzzle[i] == 16:
                if 0 <= i <= 3:
                    even = False
                elif 8 <= i <= 11:
                    even = False
                else:
                    even = True
                break

        inversion_count = helpers.inversion_count(self.puzzle)
        if even and inversion_count % 2 == 0:
            return True
        elif not even and inversion_count % 2 != 0:
            return True

        return False

    def solve(self):
        """ Solve puzzle
        Returns:
            [[int]]: solution
        """
        if not self.has_solution():
            return "Unsolvable!"
        print("Solving...")
        solution = algorithm.ida_star(self.puzzle, self.heuristic)

        return solution

    def get_puzzle(self):
        """ Returns puzzle as a list """
        return self.puzzle

    def get_heuristic(self):
        """ Returns heuristic as a string """
        return self.heuristic
