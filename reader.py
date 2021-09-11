def board_from_file(file_name):
    board = [[0 for x in range(4)] for y in range(4)]
    try:
        file = open(file_name, "r")
    except:
        return "invalid file name"
    try:
        for i in range(4):
            line = file.readline().split('\n')[0].split(' ')
            for j in range(4):
                board[i][j] = int(line[j])
    except:
        return "initialization failed"

    return board