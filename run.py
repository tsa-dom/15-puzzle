import reader
from src.app.game import Puzzle
import random
import time
from src.app.helpers import puzzle_to_string
from src.app.heuristic import manhattan_distance

def info(puzzle):
    start = time.perf_counter()
    result = puzzle.solve()
    end = time.perf_counter()
    print("Puzzle:", puzzle.get_puzzle())
    print("Time taken to solve this puzzle:", round(end - start, 3), "(seconds)")
    print("Moves needed to solve this puzzle:", len(result) - 1)
    print("Using heurisitc:", puzzle.get_heuristic())
    return result

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
        elif cmd == "init":
            try:
                puzzle_input = list(map(int, input("numbers separated by spaces > ").split(" ")))
                heuristic_input = input("heuristic name > ")
                puzzle = Puzzle(puzzle_input, heuristic_input)
                if not puzzle.has_solution():
                    print("This puzzle has no solution")
                else:
                    print("-------------------------------------------------------")
                    result = info(puzzle)
                    print("")
                    for i in result:
                        print(i)
                    print("-------------------------------------------------------")
            except:
                print("Puzzle initilization failed")
        elif cmd == "compare":
            try:    
                heuristic_1 = input("First heuristic > ")
                heuristic_2 = input("Second heuristic > ")
                count = int(input("Number of puzzles > "))
                max_manhattan = int(input("Maximum starting Manhattan distance to a puzzle > "))
                print("")
                puzzles = 0
                while puzzles < count:
                    list_to_shuffle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
                    random.shuffle(list_to_shuffle)
                    if (manhattan_distance(list_to_shuffle) > max_manhattan): continue
                    puzzle = Puzzle(list_to_shuffle, heuristic_1)
                    if puzzle.has_solution():
                        print("-------------------------------------------------------")
                        info(puzzle)
                        print("")
                        puzzle.change_heuristic(heuristic_2)
                        info(puzzle)
                        print("-------------------------------------------------------")
            except:
                print("Compare initilization failed")
        elif cmd == "help":
            print("-------------------------------------------------------")
            print("Available commands:")
            print("* help")
            print("* init (try to solve any puzzle you want to solve)")
            print("* exit")




    assert(0)

    if False:
        #puzzle = Puzzle(reader.puzzle_from_file("example.txt"), "conflict")
        puzzle = Puzzle([2, 1, 3, 4, 5, 10, 15, 11, 9, 6, 7, 8, 13, 14, 12, 16], "conflict")
        start = time.perf_counter()
        result = puzzle.solve()
        for i in result:
            print(i)
        end = time.perf_counter()
        print("-------------------------------------------------------")
        print("Puzzle:", puzzle.get_puzzle(), len(result))
        print("Time:", round(end - start, 3), "(seconds)")
        print("-------------------------------------------------------")

    manhattan_list = []
    conflict_list = []
    while len(manhattan_list) < 1:
        list_to_shuffle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        random.shuffle(list_to_shuffle)
        if (manhattan_distance(list_to_shuffle) > 50): continue
        manhattan = Puzzle(list_to_shuffle.copy(), "manhattan")
        conflict = Puzzle(list_to_shuffle.copy(), "conflict")
        if manhattan.has_solution():
            print(len(manhattan_list))
            manhattan_list.append(manhattan)
            conflict_list.append(conflict)
    print("Initialized")
    print("")
    while len(conflict_list) > 0:
        print("")
        start = time.perf_counter()
        puzzle = conflict_list.pop()
        result = puzzle.solve()
        if result == "Unsolvable!":
            continue
        end = time.perf_counter()
        print("Puzzle:", puzzle.get_puzzle(), len(result))
        print("Time:", round(end - start, 3), "(seconds)")
    print("----------------------------------------------------")
    while len(manhattan_list) > 0:
        print("")        
        start = time.perf_counter()
        puzzle = manhattan_list.pop()
        result = puzzle.solve()
        if result == "Unsolvable!":
            continue
        end = time.perf_counter()
        print("Puzzle:", puzzle.get_puzzle(), len(result))
        print("Time:", round(end - start, 3), "(seconds)")        

    while False:
        list_to_shuffle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        random.shuffle(list_to_shuffle)
        if (manhattan_distance(list_to_shuffle) >= 2): continue
        start = time.perf_counter()
        puzzle = Puzzle(list_to_shuffle, "conflict")
        result = puzzle.solve()
        if result == "Unsolvable!":
            continue
        end = time.perf_counter()
        print("Puzzle:", puzzle.get_puzzle(), len(result))
        print("Time:", round(end - start, 3), "(seconds)")