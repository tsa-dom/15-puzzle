"""
Algorithm module
"""

from src.app import heuristic
from src.app import helpers


def ida_star(puzzle, heuristic_name):
    """ IDA* algorithm
    Args:
        puzzle [int]: the initial state of the game
    Returns:
        [[[int]], int]: contains a list which contains a path and number of swaps
    """
    bound = heuristic.get_heuristic(puzzle, heuristic_name)
    path = [puzzle]

    while True:
        new_bound = search(path, 0, bound, heuristic_name)
        if new_bound == "Found":
            return path
        bound = new_bound


def search(path, g_score, bound, heuristic_name):
    """ IDA* searching algorithm
    Args:
        path [int]: current path
        g int: current path cost
        bound int: maximum cost
        path_content [string]: current path as a set
    Returns:
        type: returns "Found" or a new minimum value to cost
    """
    node = path[len(path) - 1]
    f_score = g_score + heuristic.get_heuristic(node, heuristic_name)
    if f_score > bound:
        return f_score
    if helpers.is_complete(node):
        return "Found"
    minimum = 1000000
    successors = helpers.get_successors(node, heuristic_name)
    for puzzle in successors:
        if puzzle not in path:
            path.append(puzzle)

            result = search(path, g_score + 1, bound, heuristic_name)
            if result == "Found":
                return "Found"
            if result < minimum:
                minimum = result
            path.pop()
    return minimum
