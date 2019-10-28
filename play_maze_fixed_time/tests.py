from ._builtin import Bot
import random
from .pages import Instructions, MazePage
from experiment.lottery import PreferredLotteryPairCollection, LotteryPreferencePair

class PlayerBot(Bot):
    def play_round(self):
        yield(Instructions)

        lottery_collection: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
        lottery_pair: LotteryPreferencePair = lottery_collection.selected_lottery_pair()
        yield(MazePage, {
            'solved': random.choice([0, 1]),
            'solve_time_seconds': random.randint(0, 60),
            'maze_id': lottery_pair.realized_lottery.maze.name})
