import random

from ._builtin import Bot
from .pages import Instructions, LeftMazePage, RightMazePage

from experiment.lottery import TimedLotteryPairCollection, LotteryTimedPair


class PlayerBot(Bot):

    def play_round(self):
        pass
        # yield(Instructions)
        # lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        # lottery_pair: LotteryTimedPair = lottery_collection.selected_lottery_pair()
        # yield(LeftMazePage, {
        #     'solved': random.choice([0, 1]),
        #     'solve_time_seconds': random.randint(0, lottery_pair.left_time_seconds),
        #     'maze_id': lottery_pair.left_lottery.maze.name})
        #
        # yield(RightMazePage, {
        #     'solved': random.choice([0, 1]),
        #     'solve_time_seconds': random.randint(0, lottery_pair.right_time_seconds),
        #     'maze_id': lottery_pair.right_lottery.maze.name})
