from time import time

from . import misc


PREFIX = "!"


class Cmd(object):
    def __init__(self, callables, func, cooldown=0):
        self.callables = callables
        self.func = func
        self.cooldown = cooldown
        self.next_use = time()


cmds = [
    Cmd(["marbles"], misc.marbles, cooldown=0),
    Cmd(["join"], misc.join, cooldown=5),
]


def process(bot, user, message):
    if message.startswith(PREFIX):
        cmd = message.split(" ")[0][len(PREFIX):]
        args = message.split(" ")[1:]
        perform(bot, user, cmd, *args)


def perform(bot, user, call, *args):
    for cmd in cmds:
        if call in cmd.callables:
            cmd.func(bot, user, *args)
            return
