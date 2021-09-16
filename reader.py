def puzzle_from_file(file_name):
    puzzle = []
    try:
        file = open(file_name, "r")
    except:
        return "invalid file name"
    try:
        for i in range(4):
            line = file.readline().split('\n')[0].split(' ')
            for j in range(4):
                puzzle.append(int(line[j]))
    except:
        return "initialization failed"
    return puzzle