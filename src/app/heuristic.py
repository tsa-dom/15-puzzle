from src.app import helpers
import math

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
    elif heuristic == "inversion":
        return inversion(puzzle)
    elif heuristic == "walking":
        return walking_distance(puzzle)
    elif heuristic == "euclidic":
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
        distance += math.sqrt((piece // 4 - p // 4)**2 + (piece % 4 - p % 4)**2)
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
        if piece == 15:
            continue
        if helpers.linear_conflict(puzzle, p, piece):
            conflicts += 1
    return distance + conflicts

def inversion(puzzle):
    """ Manhattan distance with inversion count
    Args:
        puzzle [int]: puzzle
    Returns:
        int: calculated Manhattan distance with inversion count
    """
    distance = 0
    horizontal_list = []
    for i in range(4):
        for j in range(4):
            horizontal_list.append(puzzle[i + j * 4])
    invc_horizontal = helpers.inversion_count(horizontal_list)
    invc_vertical = helpers.inversion_count(puzzle)
    distance += (invc_vertical / 3) + (invc_vertical % 3) + (invc_horizontal / 3) + (invc_horizontal % 3)
    return distance

def walking_distance(puzzle):
    """ Manhattan distance with walking distance
    Args:
        puzzle [int]: puzzle
    Returns:
        int: calculated Manhattan distance with walking distance
    """
    distance = 0
    for p in range(16):
        piece = puzzle[p] - 1
        if piece == 15:
            continue
        if helpers.linear_conflict(puzzle, p, piece):
            distance += 1
        distance += abs(piece // 4 - p // 4) + abs(piece % 4 - p % 4)
    invc = helpers.inversion_count(puzzle)
    distance += (invc / 3) + (invc % 3)
    return distance