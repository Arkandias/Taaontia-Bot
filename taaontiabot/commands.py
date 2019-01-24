class CommandsRegistry:
    def __init__(self):
        self.commands = {}

    def register(self, command):
        self.commands[command.trigger] = command()
        return command

    def get(self, command):
        return self.commands.get(command, HelpCommand())


class Command:
    __slots__ = ("helper", "trigger")
    subcommands = CommandsRegistry()

    def __call__(self, message):
        try:
            return self.handler(message)
        except NotImplementedError:
            return self.subcommands.get(message[0])(message[1:])

    def handler(self):
        raise NotImplementedError()


commands = CommandsRegistry()


@commands.register
class SuccessCommand(Command):
    helper = "Try something."
    trigger = "succeed"

    def __call__(event, message):
        return "You successfully failed"


@commands.register
class FailCommand(Command):
    helper = "Try something."
    trigger = "fail"

    def __call__(event, message):
        return "You tried something. You failed"


@commands.register
class TravelCommand(Command):
    helper = "Try to move a bit ."
    trigger = "travel"

    def __call__(event, message):
        return "You travel a bit to try to change your peevish, poor life. You failed."


@commands.register
class DungeonCommand(Command):
    helper = "Try to explore a dungeon."
    trigger = "dungeon"

    def __call__(event, message):
        return "A latex-covered dominatrix comes to you with a leather whip. You undestand that's not the kind of dungeon you want to explore."


@commands.register
class HelpCommand(Command):
    helper = "Show this help."
    trigger = "help"

    def __call__(event, message):
        if message:
            return commands.get(message).helper
        ret = "```"
        for _, command in commands.commands.items():
            ret += "{} - {}\n".format(command.trigger, command.helper)
            for _, subCommand in command.subcommands.commands.items():
                ret += "\t{} - {}\n".format(subCommand.trigger, subCommand.helper)
        return ret + "```"
