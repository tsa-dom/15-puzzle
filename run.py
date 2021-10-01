import reader
from src.app.game import Puzzle
import random
import time
from src.app.helpers import puzzle_to_string

# Some failure attempts to implement Walking distance heuristic
"""def sort(puzzle):
    l1 = puzzle[0:4].copy()
    l2 = puzzle[4:8].copy()
    l3 = puzzle[8:12].copy()
    l4 = puzzle[12:16].copy()
    l1.sort()
    l2.sort()
    l3.sort()
    l4.sort()

    result = []
    for i in range(4):
        result.append(l1[i])
    for i in range(4):
        result.append(l2[i])
    for i in range(4):
        result.append(l3[i])
    for i in range(4):
        result.append(l4[i])
    return result


def generate_all(puzzle, graph, include, sixteen, counter):
    if counter > 3: return
    if puzzle_to_string(sort(puzzle)) in include:
        print(sort(puzzle))
        return
    include.add(puzzle_to_string(sort(puzzle)))
    line = sixteen // 4
    if line > 0:
        for i in range(4):
            new_puzzle = puzzle.copy()
            new_puzzle[sixteen], new_puzzle[(line - 1) * 4 + i] = new_puzzle[(line - 1) * 4 + i], new_puzzle[sixteen]
            generate_all(new_puzzle ,graph, include, (line - 1) * 4 + i, counter + 1)
    if line < 3:
        for i in range(4):
            new_puzzle = puzzle.copy()
            new_puzzle[sixteen], new_puzzle[(line - 1) * 4 + i] = new_puzzle[(line - 1) * 4 + i], new_puzzle[sixteen]
            generate_all(new_puzzle ,graph, include, (line + 1) * 4 + i, counter + 1)
    return len(include)"""


if __name__ == "__main__":
    """ Main method """

    # Available heuristics:
    # - conflict
    # - euclidic
    # - misplaced
    # - manhattan (default)

    if False:
        puzzle = Puzzle(reader.puzzle_from_file("example.txt"), "conflict")
        start = time.perf_counter()
        result = puzzle.solve()
        #for i in result:
        #    print(i)
        end = time.perf_counter()
        print("-------------------------------------------------------")
        print("Puzzle:", puzzle.get_puzzle(), len(result))
        print("Time:", round(end - start, 3), "(seconds)")

    while True:
        list_to_shuffle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        random.shuffle(list_to_shuffle)
        start = time.perf_counter()
        puzzle = Puzzle(list_to_shuffle, "conflict")
        result = puzzle.solve()
        if result == "Unsolvable!":
            continue
        end = time.perf_counter()
        print("Puzzle:", puzzle.get_puzzle(), len(result))
        print("Time:", round(end - start, 3), "(seconds)")