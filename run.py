import reader
from solver import Puzzle
import random
import time

if __name__ == "__main__":
    """ Main method """

    puzzle = Puzzle(reader.puzzle_from_file("example.txt"))
    puzzle.solve()
    while False:
        start = time.perf_counter()
        mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        random.shuffle(mylist)
        test = Puzzle(mylist)
        result = test.solve()
        if result == "Unsolvable!":
            continue
        end = time.perf_counter()
        print(result, round(end - start, 3))
    while False:
        cmd = input("cmd > ")
        if (cmd == "init"):
            #file = input("filename: ")
            puzzle = reader.puzzle_from_file("example.txt")
            print(solution_finder.has_solution(puzzle))

        elif (cmd == "exit"):
            break