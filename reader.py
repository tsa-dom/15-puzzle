def puzzle_from_file(file_name):
    """ File reading functionality
    Args:
        file_name string: name of the file to be read
    Returns:
        [int]: a puzzle if reading success and an error if not
    """
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