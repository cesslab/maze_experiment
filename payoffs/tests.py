from ._builtin import Bot

from .pages import Payoffs


class PlayerBot(Bot):
    def play_round(self):
        yield(Payoffs)
