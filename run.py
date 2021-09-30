import reader
from src.app.game import Puzzle
import random
import time

if __name__ == "__main__":
    """ Main method """

    # Available heuristics:
    # - conflict
    # - inversion
    # - walking
    # - manhattan (default)

    if False:
        puzzle = Puzzle(reader.puzzle_from_file("example.txt"), "euclidic")
        start = time.perf_counter()
        result = puzzle.solve()
        #for i in result:
        #    print(i)
        end = time.perf_counter()
        print("-------------------------------------------------------")
        print("Puzzle:", puzzle.get_puzzle(), len(result))
        print("Time:", round(end - start, 3), "(seconds)")

    if True:
        puzzle = Puzzle(reader.puzzle_from_file("example.txt"), "inversion")
        start = time.perf_counter()
        result = puzzle.solve()
        end = time.perf_counter()
        print("-------------------------------------------------------")
        print("Puzzle:", puzzle.get_puzzle(), len(result))
        print("Time:", round(end - start, 3), "(seconds)")

    while False:
        list_to_shuffle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        random.shuffle(list_to_shuffle)
        start = time.perf_counter()
        puzzle = Puzzle(list_to_shuffle, "manhattan")
        result = puzzle.solve()
        if result == "Unsolvable!":
            continue
        end = time.perf_counter()
        print(len(result), result[0], round(end - start, 3))

        start = time.perf_counter()
        puzzle = Puzzle(list_to_shuffle, "inversion")
        result = puzzle.solve()
        if result == "Unsolvable!":
            continue
        end = time.perf_counter()
        print(len(result), result[0], round(end - start, 3))