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
    elif heuristic == "inversion":
        return manhattan_inversion(puzzle)
    elif heuristic == "walking":
        return walking_distance(puzzle)
    else:
        return manhattan_distance(puzzle)

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

def manhattan_linear_conflict(puzzle):
    """ Mangattan distance with linear conflict
    Args:
        puzzle [int]: puzzle
    Returns:
        int: calculated Manhattan distance with linear conflict
    """
    distance = 0
    for p in range(16):
        piece = puzzle[p] - 1
        if piece == 15:
            continue
        if helpers.linear_conflict(puzzle, p, piece):
            distance += 1
        distance += abs(piece // 4 - p // 4) + abs(piece % 4 - p % 4)
    return distance

def manhattan_inversion(puzzle):
    """ Manhattan distance with inversion count
    Args:
        puzzle [int]: puzzle
    Returns:
        int: calculated Manhattan distance with inversion count
    """
    distance = 0
    for p in range(16):
        piece = puzzle[p] - 1
        if piece == 15:
            continue
        distance += abs(piece // 4 - p // 4) + abs(piece % 4 - p % 4)
    invc_vertical = helpers.inversion_count(puzzle)
    distance += (invc_vertical / 3) + (invc_vertical % 3)
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