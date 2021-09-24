import time


def ida_star(puzzle):
    """ IDA* algorithm

    Args:
        puzzle ([int]): the initial state of the game

    Returns:
        [[[int]], int]: contains a list which contains a path and a number of swaps
    """
    bound = manhattan_distance(puzzle)
    path = [puzzle]
    path_content = set()
    path_content.add(puzzle_to_string(puzzle))
    while True:
        new_bound = search(path, 0, bound, path_content)
        if new_bound == "Found":
            return [path, bound]
        bound = new_bound

def search(path, g, bound, path_content):
    """ IDA* searching algorithm

    Args:
        path ([int]): current path
        g (int): current path cost
        bound (int): maximum cost
        path_content ([string]): current path as a set

    Returns:
        type : returns "Found" or a new minimum value to cost 
    """
    node = path[len(path) - 1]
    f = g + manhattan_distance(node)
    if f > bound:
        return f
    if is_complete(node):
        return "Found"
    min = 1000000
    successors = get_successors(node)
    for puzzle in successors:
        puzzle_str = puzzle_to_string(puzzle)
        if puzzle_to_string(puzzle) not in path_content:
            path.append(puzzle)
            path_content.add(puzzle_str)

            result = search(path, g + manhattan_distance(puzzle) - manhattan_distance(node) + 1, bound, path_content)
            if result == "Found":
                return "Found"
            if result < min:
                min = result
            path_content.remove(puzzle_str)
            path.pop()
    return min

def swap(puzzle, i, j):
    """ Swaps two puzzle pieces

    Args:
        puzzle ([int]): the puzzle to be swapped
        i (int): puzzle list index
        j (int): puzzle list index

    Returns:
        [int]: new puzzle with swapped tiles
    """
    swap = puzzle.copy()
    swap[i], swap[j] = swap[j], swap[i]
    return swap

def get_successors(node):
    """ Finds all node successors and sorts them depending on Manhattan distance

    Args:
        node ([int]): current puzzle state as a node

    Returns:
        [[int]]: list of node children
    """
    x = find_16(node) + 1
    p1, p2, p3, p4 = None, None, None, None
    successors = []
    if x + 4 <= 16:
        p1 = x + 4
    if x - 4 >= 1:
        p2 = x - 4
    if x % 4 != 0:
        p3 = x + 1
    if x - 1 % 4 != 0:
        p4 = x - 1

    if p1 != None:
        successors.append(swap(node, x - 1, p1 - 1))
    if p2 != None:
        successors.append(swap(node, x - 1, p2 - 1))
    if p3 != None:
        successors.append(swap(node, x - 1, p3 - 1))
    if p4 != None:
        successors.append(swap(node, x - 1, p4 - 1))

    successors.sort(key=manhattan_distance)

    return successors


def find_16(puzzle):
    """ Finds a puzzle index with value 16

    Args:
        puzzle ([int]): puzzle

    Returns:
        int: the index where the number 16 is in the puzzle
    """
    for i in range(16):
        if puzzle[i] == 16:
            return i

def puzzle_to_string(puzzle):
    """ Method to convert puzzle array to string

    Args:
        puzzle ([int]): puzzle

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

"""
* * * *
* x * *
* 6 * *
* * * *
x => 5
6 => 9
* * * *
* x 6 *
* * * *
* * * *
x => 5
6 => 6
"""
def linear_conflict(puzzle, i, j):
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

def manhattan_distance(puzzle):
    """ Manhattan distance calculation method

    Args:
        puzzle ([int]): puzzle

    Returns:
        int: calculated Manhattan distance
    """
    distance = 0
    for p in range(16):
        piece = puzzle[p] - 1
        if piece == 15:
            continue
        if linear_conflict(puzzle, p, piece):
            distance += 1
        distance += abs(piece // 4 - p // 4) + abs(piece % 4 - p % 4)
    return distance

def manhattan_linear_conflict(puzzle):
    distance = 0
    for p in range(16):
        piece = puzzle[p] - 1
        if piece == 15:
            continue
        if linear_conflict(puzzle, p, piece):
            distance += 1
        distance += abs(piece // 4 - p // 4) + abs(piece % 4 - p % 4)
    return distance

def walking_distance(puzzle):
    distance = 0
    for p in range(16):
        piece = puzzle[p] - 1
        if piece == 15:
            continue
        distance += abs(piece // 4 - p // 4) + abs(piece % 4 - p % 4)
    return distance

def is_complete(puzzle):
    """ Checks if a given puzzle is completed

    Args:
        puzzle ([int]): puzzle

    Returns:
        [bool]: true if puzzle is completed and false if not
    """
    for i in range(16):
        if i + 1 != puzzle[i]:
            return False
    return True