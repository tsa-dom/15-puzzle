from src.app import algorithm
from src.app import helpers

class Puzzle:
    
    def __init__(self, puzzle, heuristic):
        """ A new puzzle initialization function
        Args:
            puzzle [int]: desired puzzle initial state
        """
        self.puzzle = puzzle
        self.heuristic = heuristic

    def change_heuristic(self, heuristic):
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
        return self.puzzle