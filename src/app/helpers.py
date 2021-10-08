"""
Useful helper functions
"""

from src.app import heuristic # pylint: disable=import-error

def swap(puzzle, i, j):
    """ Swaps two puzzle pieces
    Args:
        puzzle [int]: the puzzle to be swapped
        i int: puzzle list index
        j int: puzzle list index
    Returns:
        [int]: new puzzle with swapped tiles
    """
    swap = puzzle.copy()
    swap[i], swap[j] = swap[j], swap[i]
    return swap

def get_successors(node, heuristic_name):
    """ Finds all node successors and sorts them depending on Manhattan distance
    Args:
        node [int]: current puzzle state as a node
    Returns:
        [[int]]: list of node children
    """
    x = find_16(node) + 1
    successors = []
    if x + 4 <= 16:
        successors.append(swap(node, x - 1, x + 3))
    if x - 4 >= 1:
        successors.append(swap(node, x - 1, x - 5))
    if x % 4 != 0:
        successors.append(swap(node, x - 1, x))
    if (x - 1) % 4 != 0:
        successors.append(swap(node, x - 1, x - 2))

    successors.sort(key=lambda x: heuristic.get_heuristic(x, heuristic_name))

    return successors


def find_16(puzzle):
    """ Finds a puzzle index with value 16
    Args:
        puzzle [int]: puzzle
    Returns:
        int: the index where the number 16 is in the puzzle
    """
    for i in range(16):
        if puzzle[i] == 16:
            return i

def puzzle_to_string(puzzle):
    """ Method to convert puzzle array to string
    Args:
        puzzle [int]: puzzle
    Returns:
        string: string value of the puzzle state
    """
    string = ""
    for i in puzzle:
        if i < 10:
            string += str(i)
        elif i == 10:
            string += "a"
        elif i == 11:
            string += "b"
        elif i == 12:
            string += "c"
        elif i == 13:
            string += "d"
        elif i == 14:
            string += "e"
        elif i == 15:
            string += "f"
        else:
            string += "x"
    
    return string

def is_complete(puzzle):
    """ Checks if a given puzzle is completed
    Args:
        puzzle [int]: puzzle
    Returns:
        bool: true if puzzle is completed and false if not
    """
    for i in range(16):
        if i + 1 != puzzle[i]:
            return False
    return True

def inversion_count(puzzle):
    """ Inversion count calculation method
    Args:
        puzzle [int]: puzzle
    Returns:
        int: the number of inversions
    """
    inversion_list = []
    for i in range(16):
        if puzzle[i] == 16:
            continue
        inversion_list.append(puzzle[i])

    target = 15
    inversion_count = 0
    while target > 1:
        pointer = 0
        while pointer < target - 1:
            if inversion_list[pointer] == target:
                inversion_list[pointer], inversion_list[pointer + 1] = inversion_list[pointer + 1], inversion_list[pointer]
                inversion_count += 1
            pointer += 1

        target -= 1
    return inversion_count

def linear_conflict(puzzle, i, j):
    """ Check linear conflicts with two tiles
    Args:
        puzzle [int]: puzzle
        i int: first tile
        j int: second tile
    Returns:
        bool: true if there is linear conflict and false if not
    """
    if i != puzzle[j] - 1 or i == j:
        return False
    if (i - j) % 4 == 0:
        return True
    if 0 <= i < 4 and 0<= j < 4:
        return True
    if 4 <= i < 8 and 4<= j < 8:
        return True
    if 8 <= i < 12 and 8<= j < 12:
        return True
    if 12 <= i < 16 and 12<= j < 16:
        return True
    return False