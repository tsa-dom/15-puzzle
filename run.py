""" Run module """

import time
import random
from reader import puzzle_from_file
from src.app.game import Puzzle
from src.app.heuristic import manhattan_distance

def info(puzzle):
    """ Print info """

    start = time.perf_counter()
    result = puzzle.solve()
    end = time.perf_counter()
    print("Puzzle:", puzzle.get_puzzle())
    print("Time taken to solve this puzzle:", round(end - start, 3), "(seconds)")
    print("Moves needed to solve this puzzle:", len(result) - 1)
    print("Using heurisitc:", puzzle.get_heuristic())
    return result

def heuristic_names():
    """ List all available heuristics """

    print("-------------------------------------------------------")
    print("Available heuristics")
    print("* manhattan (Manhattan distance, default")
    print("* conflict (Linear conflict with Manhattan distance")
    print("* euclid (Euclid distance)")
    print("* misplaced (Misplaced distance, actually so slow that it's almost useless)")
    print("-------------------------------------------------------")

def result_tree(puzzle):
    print("-------------------------------------------------------")
    result = info(puzzle)
    print("")
    for i in result:
        print(i)
    print("-------------------------------------------------------")

if __name__ == "__main__":
    """ Main method """

    # Available heuristics:
    # - conflict
    # - euclidic
    # - misplaced
    # - manhattan (default)

    puzzle = Puzzle([2, 1, 3, 4, 5, 10, 15, 11, 9, 6, 7, 8, 13, 14, 12, 16], "conflict")

    while True:
        cmd = input("cmd > ")
        if cmd == "exit":
            break
        elif cmd == "solve":
            heuristic_names()
            try:
                puzzle_input = list(map(int, input("puzzle initial state as numbers separated by spaces: ").split(" ")))
                heuristic_input = input("heuristic name: ")
                puzzle = Puzzle(puzzle_input, heuristic_input)
                if not puzzle.has_solution():
                    print("This puzzle has no solution")
                else:
                    result_tree(puzzle)
            except:
                print("Puzzle initialization failed")
        elif cmd == "file":
            heuristic_names()
            try:
                file_name = input("specify file name to read (default example.txt): ")
                heuristic_name = input("heuristic name: ")
                if (file_name == ""):
                    file_name = "example.txt"
                puzzle_state = puzzle_from_file(file_name)
                puzzle = Puzzle(puzzle_state, heuristic_name)
                if not puzzle.has_solution():
                    print("This puzzle has no solution")
                else:
                    result_tree(puzzle)
            except:
                print("Puzzle initialization failed")

        elif cmd == "compare":
            try:
                heuristic_names()
                heuristic_1 = input("first heuristic: ")
                heuristic_2 = input("second heuristic: ")
                count = int(input("number of puzzles: "))
                max_manhattan = int(input("maximum starting Manhattan distance to a puzzle: "))
                print("")
                PUZZLES = 0
                while PUZZLES < count:
                    list_to_shuffle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
                    random.shuffle(list_to_shuffle)
                    if (manhattan_distance(list_to_shuffle) > max_manhattan):
                        continue
                    puzzle = Puzzle(list_to_shuffle, heuristic_1)
                    if puzzle.has_solution():
                        print("-------------------------------------------------------")
                        info(puzzle)
                        print("")
                        puzzle.change_heuristic(heuristic_2)
                        info(puzzle)
                        print("-------------------------------------------------------")
                        PUZZLES += 1
            except: 
                print("Compare initilization failed")
        elif cmd == "help":
            print("-------------------------------------------------------")
            print("Available commands:")
            print("* help       (list all available commands)")
            print("* solve      (try to solve any puzzle you want to solve)")
            print("* compare    (compare efficiency between two heuristics)")
            print("* file       (read initial state from the file)")
            print("* exit       (close program)")
            print("-------------------------------------------------------")
    print("Bye")