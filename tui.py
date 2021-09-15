import solution_finder

def run(reader):
    puzzle = reader.puzzle_from_file("example.txt")
    print(solution_finder.has_solution(puzzle))
    while False:
        cmd = input("cmd > ")
        if (cmd == "init"):
            #file = input("filename: ")
            puzzle = reader.puzzle_from_file("example.txt")
            print(solution_finder.has_solution(puzzle))

        elif (cmd == "exit"):
            break