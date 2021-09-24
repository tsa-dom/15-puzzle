import reader
from solver import Puzzle
import random
import time
import helpers

if __name__ == "__main__":
    """ Main method """

    t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    s = [15, 2, 11, 5, 4, 7, 6, 8, 12, 10, 3, 9, 13, 14, 1, 16]
    print(s)
    for i in range(16):
        print(i, s[i]-1, helpers.linear_conflict(s, i, s[i] - 1))

    #print(helpers.manhattan_distance([2, 16, 7, 10, 5, 15, 13, 6, 11, 12, 14, 8, 4, 9, 1, 3]))

    if True:
        print(helpers.manhattan_distance([6, 13, 7, 16, 8, 9, 12, 11, 15, 2, 10, 5, 14, 3, 1, 4]))
        puzzle = Puzzle(reader.puzzle_from_file("example.txt"))
        start = time.perf_counter()
        result = puzzle.solve()
        end = time.perf_counter()
        print(result, round(end - start, 3))
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