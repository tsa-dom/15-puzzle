"""
Useful helper functions
"""

from src.app import heuristic


def swap_puzzle(puzzle, i, j):
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
    x16 = find_16(node) + 1
    successors = []
    if x16 + 4 <= 16:
        successors.append(swap_puzzle(node, x16 - 1, x16 + 3))
    if x16 - 4 >= 1:
        successors.append(swap_puzzle(node, x16 - 1, x16 - 5))
    if x16 % 4 != 0:
        successors.append(swap_puzzle(node, x16 - 1, x16))
    if (x16 - 1) % 4 != 0:
        successors.append(swap_puzzle(node, x16 - 1, x16 - 2))

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
    return None


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
    inv_list = []
    for i in range(16):
        if puzzle[i] == 16:
            continue
        inv_list.append(puzzle[i])

    target = 15
    inversions = 0
    while target > 1:
        ptr = 0
        while ptr < target - 1:
            if inv_list[ptr] == target:
                inv_list[ptr], inv_list[ptr + 1] = inv_list[ptr + 1], inv_list[ptr]
                inversions += 1
            ptr += 1

        target -= 1
    return inversions


def linear_conflict(puzzle, i, j):
    """ Check linear conflicts with two tiles
    Args:
        puzzle [int]: puzzle
        i int: first tile
        j int: second tile
    Returns:
        bool: true if there is linear conflict and false if not
    """
    return (i == puzzle[j] - 1 and i != j) \
        and ((i - j) % 4 == 0 \
        or (0 <= i < 4 and 0 <= j < 4) \
        or (4 <= i < 8 and 4 <= j < 8) \
        or (8 <= i < 12 and 8 <= j < 12) \
        or (12 <= i < 16 and 12 <= j < 16))
