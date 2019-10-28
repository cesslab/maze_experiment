from ._builtin import Bot
import random
from .pages import Instructions, PracticeMaze


class PlayerBot(Bot):
    def play_round(self):
        yield(Instructions)
        yield(PracticeMaze, {'solved': random.choice([0, 1]), 'solve_time_seconds': 60, 'maze_id': 'closed'})

