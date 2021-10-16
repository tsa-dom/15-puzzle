"""
File reader
"""


def puzzle_from_file(file_name):
    """ File reading functionality
    Args:
        file_name string: name of the file to be read
    Returns:
        [int]: a puzzle if reading success and an error if not
    """
    puzzle = []
    try:
        file = open(file_name, "r", encoding="utf-8")
    except BaseException:
        return "invalid file name"
    try:
        for _ in range(4):
            line = file.readline().split('\n')[0].split(' ')
            for j in range(4):
                puzzle.append(int(line[j]))
    except BaseException:
        return "initialization failed"
    return puzzle
