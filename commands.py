class Command:
    __slots__ = (
        'helper',
        'action'
    )
    pass

class SuccessCommand(Command):
    helper = 'Try something.'
    action = 'success'
    def __call__(event):
        return 'You successfully failed'
    pass

class FailCommand(Command):
    helper = 'Try something.'
    action = 'fail'
    def __call__(event):
        return 'You tried something. You failed'
    pass

class TravelCommand(Command):
    helper = 'Try to move a bit .'
    action = 'travel'
    def __call__(event):
        return 'You travel a bit to try to change your peevish, poor life. You failed.'
    pass

class DungeonCommand(Command):
    helper = 'Try to explore a dungeon.'
    action = 'dungeon'
    def __call__(event):
        return 'A latex-covered dominatrix comes to you with a leather whip. You undestand that\'s not the kind of dungeon you want to explore.'
    pass

class HelperCommand(Command):
    helper = 'Show this help.'
    action = 'helper'
    def __call__(event):
        ret = "```"
        for command in Command.__subclasses__():
            ret += '{} - {}\n'.format(command.action, command.helper)
        return ret + '```';
    pass    


commands = {command.action: command() for command in Command.__subclasses__()}
