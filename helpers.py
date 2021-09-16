def ida_star(puzzle):
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

            result = search(path, g + manhattan_distance(puzzle) - manhattan_distance(node), bound, path_content)
            if result == "Found":
                return "Found"
            if result < min:
                min = result
            path_content.remove(puzzle_str)
            path.pop()
    return min

def swap(puzzle, i, j):
    swap = puzzle.copy()
    swap[i], swap[j] = swap[j], swap[i]
    return swap

def get_successors(node):
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
    for i in range(16):
        if puzzle[i] == 16:
            return i

def puzzle_to_string(puzzle):
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

def manhattan_distance(puzzle):
    distance = 0
    for p in range(16):
        piece = puzzle[p] - 1
        if piece == 15:
            continue
        distance += abs(piece // 4 - p // 4) + abs(piece % 4 - p % 4)
    return distance

def is_complete(puzzle):
    for i in range(16):
        if i + 1 != puzzle[i]:
            return False
    return True