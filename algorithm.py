import heuristic
import helpers

def ida_star(puzzle, heuristic_name):
    """ IDA* algorithm
    Args:
        puzzle [int]: the initial state of the game
    Returns:
        [[[int]], int]: contains a list which contains a path and a number of swaps
    """
    bound = heuristic.get_heuristic(puzzle, heuristic_name)
    path = [puzzle]
    path_content = set()
    path_content.add(helpers.puzzle_to_string(puzzle))
    while True:
        new_bound = search(path, 0, bound, path_content, heuristic_name)
        if new_bound == "Found":
            return path
        bound = new_bound

def search(path, g, bound, path_content, heuristic_name):
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
    f = g + heuristic.get_heuristic(node, heuristic_name)
    if f > bound:
        return f
    if helpers.is_complete(node):
        return "Found"
    min = 1000000
    successors = helpers.get_successors(node, heuristic_name)
    for puzzle in successors:
        puzzle_str = helpers.puzzle_to_string(puzzle)
        if helpers.puzzle_to_string(puzzle) not in path_content:
            path.append(puzzle)
            path_content.add(puzzle_str)

            result = search(path, g + heuristic.get_heuristic(puzzle, heuristic_name) - heuristic.get_heuristic(node, heuristic_name) + 1, bound, path_content, heuristic_name)
            if result == "Found":
                return "Found"
            if result < min:
                min = result
            path_content.remove(puzzle_str)
            path.pop()
    return min