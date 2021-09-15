def has_solution(puzzle):
    inversion_list = []

    even = None
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == 16:
                if i % 2 == 0:
                    even = False
                else:
                    even = True
                continue
            inversion_list.append(puzzle[i][j])

    target = 15
    inversion_count = 0
    while target > 1:
        pointer = 0
        while pointer < target - 1:
            if inversion_list[pointer] == target:
                inversion_list[pointer], inversion_list[pointer + 1] = inversion_list[pointer + 1], inversion_list[pointer]
                inversion_count += 1
            pointer += 1

        target -= 1
        
    if even and inversion_count % 2 == 0:
        return True
    elif not even and inversion_count % 2 != 0:
        return True

    return False