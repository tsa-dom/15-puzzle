"""
All used heuristics are stored here
"""

from math import sqrt
from src.app import helpers # pylint: disable=import-error

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
    elif heuristic == "euclid":
        return euclid_distance(puzzle)
    elif heuristic == "misplaced":
        return misplaced_distance(puzzle)
    else:
        return manhattan_distance(puzzle)

def misplaced_distance(puzzle):
    distance = 0
    for p in range(16):
        piece = puzzle[p] - 1
        if piece == 15:
            continue
        else:
            if piece == p:
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
    for p in range(16):
        piece = puzzle[p] - 1
        if piece == 15:
            continue
        distance += abs(piece // 4 - p // 4) + abs(piece % 4 - p % 4)
    return distance

def euclid_distance(puzzle):
    distance = 0
    for p in range(16):
        piece = puzzle[p] - 1
        if piece == 15:
            continue
        distance += sqrt((piece // 4 - p // 4)**2 + (piece % 4 - p % 4)**2)
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
    for p in range(16):
        piece = puzzle[p] - 1
        if piece == 15:
            continue
        distance += abs(piece // 4 - p // 4) + abs(piece % 4 - p % 4)
    for p in range(16):
        piece = puzzle[p] - 1
        if piece == 15 or p == 15:
            continue
        if helpers.linear_conflict(puzzle, p, piece):
            conflicts += 1
    return distance + conflicts