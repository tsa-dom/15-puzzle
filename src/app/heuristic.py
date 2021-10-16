"""
All used heuristics are stored here
"""

from math import sqrt
from src.app import helpers


def get_heuristic(puzzle, heuristic):
    """ Heuristic function getter
    Args:
        puzzle [int]: puzzle
        heuristic str: heuristic name
    Returns:
        function: heuristic function with a puzzle param
    """
    if heuristic == "conflict":
        return manhattan_linear_conflict(puzzle)
    if heuristic == "euclid":
        return euclid_distance(puzzle)
    if heuristic == "misplaced":
        return misplaced_distance(puzzle)
    return manhattan_distance(puzzle)


def misplaced_distance(puzzle):
    """ Misplaced distance calculation method
    Args:
        puzzle [int]: puzzle
    Returns:
        int: calculated Misplaced distance
    """
    distance = 0
    for i in range(16):
        piece = puzzle[i] - 1
        if not piece == 15 and piece == i:
            distance += 1
    return distance


def manhattan_distance(puzzle):
    """ Manhattan distance calculation method
    Args:
        puzzle [int]: puzzle
    Returns:
        int: calculated Manhattan distance
    """
    distance = 0
    for i in range(16):
        piece = puzzle[i] - 1
        if piece == 15:
            continue
        distance += abs(piece // 4 - i // 4) + abs(piece % 4 - i % 4)
    return distance


def euclid_distance(puzzle):
    """ Euclid distance calculation method
    Args:
        puzzle [int]: puzzle
    Returns:
        int: calculated Euclid distance
    """
    distance = 0
    for i in range(16):
        piece = puzzle[i] - 1
        if piece == 15:
            continue
        distance += sqrt((piece // 4 - i // 4)**2 + (piece % 4 - i % 4)**2)
    return distance


def manhattan_linear_conflict(puzzle):
    """ Mangattan distance with linear conflict
    Args:
        puzzle [int]: puzzle
    Returns:
        int: calculated Manhattan distance with linear conflict
    """
    distance = 0
    conflicts = 0
    for i in range(16):
        piece = puzzle[i] - 1
        if piece == 15:
            continue
        distance += abs(piece // 4 - i // 4) + abs(piece % 4 - i % 4)
    for i in range(16):
        piece = puzzle[i] - 1
        if piece == 15 or i == 15:
            continue
        if helpers.linear_conflict(puzzle, i, piece):
            conflicts += 1
    return distance + conflicts
