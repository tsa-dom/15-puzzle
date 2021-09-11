def run(reader):
    while True:
        cmd = input("cmd > ")
        if (cmd == "init"):
            file = input("filename: ")
            print(reader.board_from_file(file))
        elif (cmd == "exit"):
            break