from solver import Puzzle

def run(reader):
    puzzle = Puzzle(reader.puzzle_from_file("example.txt"))
    print(puzzle.has_solution())
    print(puzzle.solve())
    while False:
        cmd = input("cmd > ")
        if (cmd == "init"):
            #file = input("filename: ")
            puzzle = reader.puzzle_from_file("example.txt")
            print(solution_finder.has_solution(puzzle))

        elif (cmd == "exit"):
            break