def ida_star(puzzle):
    bound = manhattan_distance(puzzle)
    path = [puzzle]
    path_content = set()
    path_content.add(puzzle_to_string(puzzle))
    while True:
        new_bound = search(path, 0, bound)
        if new_bound == "Found":
            return [path, bound]
        bound = new_bound
        

def search(path, g, bound):
    node = path[len(path) - 1]
    f = g + manhattan_distance(node)
    if f > bound:
        return f
    if is_complete(node):
        return "Found"
    min = 1000000

def successors(node):
    x = find_16(node)



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