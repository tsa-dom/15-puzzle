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

    if True:
        puzzle = Puzzle(reader.puzzle_from_file("example.txt"), "manhattan")
        start = time.perf_counter()
        result = puzzle.solve()
        for i in result:
            print(i)
        end = time.perf_counter()
        print("-------------------------------------------------------")
        print("Puzzle:", puzzle.get_puzzle())
        print("Time:", round(end - start, 3), "(seconds)")

    while False:
        start = time.perf_counter()
        list_to_shuffle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        random.shuffle(list_to_shuffle)
        puzzle = Puzzle(list_to_shuffle, "inversion")
        result = puzzle.solve()
        if result == "Unsolvable!":
            continue
        end = time.perf_counter()
        print(result[0], round(end - start, 3))