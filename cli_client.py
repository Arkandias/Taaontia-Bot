from taaontiabot.commands import commands


def test():
    while True:
        rawcommand = input("> Type in a command:\n> ")
        if rawcommand == "exit":
            break
        parsed_message = rawcommand.split(" ", 2)
        print(commands.get(parsed_message[0])(parsed_message[1]))


if __name__ == "__main__":
    test()

