class Command:
    __slots__ = (
        'helper',
        'trigger',
        'subCommand'
    )
    def __call__(self):
        raise NotImplementedError()

class CommandsRegistry:
    def __init__(self):
        self.commands = {}
    def register(self, command):
        self.commands[command.trigger] = command()
        return command
    def get(self, command):
        return self.commands.get(command, HelpCommand())

commands = CommandsRegistry()

@commands.register
class SuccessCommand(Command):
    helper = 'Try something.'
    trigger = 'success'
    subCommand = CommandsRegistry()
    def __call__(event):
        return 'You successfully failed'

@commands.register
class FailCommand(Command):
    helper = 'Try something.'
    trigger = 'fail'
    subCommand = CommandsRegistry()
    def __call__(event, message):
        return 'You tried something. You failed'

@commands.register
class TravelCommand(Command):
    helper = 'Try to move a bit .'
    trigger = 'travel'
    subCommand = CommandsRegistry()
    def __call__(event, message):
        return 'You travel a bit to try to change your peevish, poor life. You failed.'

@commands.register
class DungeonCommand(Command):
    helper = 'Try to explore a dungeon.'
    trigger = 'dungeon'
    subCommand = CommandsRegistry()
    def __call__(event, message):
        return 'A latex-covered dominatrix comes to you with a leather whip. You undestand that\'s not the kind of dungeon you want to explore.'

@commands.register
class HelpCommand(Command):
    helper = 'Show this help.'
    trigger = 'help'
    subCommand = CommandsRegistry()
    def __call__(event, message):
        ret = "```"
        for commandKey, command in commands.commands.items():
            ret += '{} - {}\n'.format(command.trigger, command.helper)
            for subCommandKey, subCommand in command.subCommand.commands.items():
                ret += '\t{} - {}\n'.format(subCommand.trigger, subCommand.helper)
        return ret + '```'
