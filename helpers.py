def puzzle_to_string(puzzle):
    string = ""
    for i in range(4):
        for j in range(4):
            piece = puzzle[i][j]
            if piece < 10:
                string += str(piece)
            elif piece == 10:
                string += "a"
            elif piece == 11:
                string += "b"
            elif piece == 12:
                string += "c"
            elif piece == 13:
                string += "d"
            elif piece == 14:
                string += "e"
            elif piece == 15:
                string += "f"
            else:
                string += "x"
    
    return string

# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16

# 13 2  10 3    3 0 3 1
# 1  12 8  4    1 3 1 1
# 5  16 9  6    1 3 2 3
# 15 14 11 7    2 0 1

# 7 + 6 + 9 + 3 = 25

def manhattan_distance(puzzle):
    distance = 0
    for i in range(4):
        for j in range(4):
            piece = puzzle[i][j]
            if piece == 1:
                distance += i + j
            elif piece == 2:
                distance += i + abs(j - 1)
            elif piece == 3:
                distance += i + abs(j - 2)
            elif piece == 4:
                distance += i + abs(j - 3)
            elif piece == 5:
                distance += abs(i - 1) + j
            elif piece == 6:
                distance += abs(i - 1) + abs(j - 1)
            elif piece == 7:
                distance += abs(i - 1) + abs(j - 2)
            elif piece == 8:
                distance += abs(i - 1) + abs(j - 3)
            elif piece == 9:
                distance += abs(i - 2) + j
            elif piece == 10:
                distance += abs(i - 2) + abs(j - 1)
            elif piece == 11:
                distance += abs(i - 2) + abs(j - 2)
            elif piece == 12:
                distance += abs(i - 2) + abs(j - 3)
            elif piece == 13:
                distance += abs(i - 3) + j
            elif piece == 14:
                distance += abs(i - 3) + abs(j - 1)
            elif piece == 15:
                distance += abs(i - 3) + abs(j - 2)

    return distance