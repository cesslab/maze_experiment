import random

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from experiment.mazes import Maze
from experiment.lottery import Lottery, LotteryTimedPair, TimedLotteryPairCollection


class Constants(BaseConstants):
    name_in_url = 'time_allocation'
    players_per_group = None
    num_rounds = 4


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            lottery_pairs = TimedLotteryPairCollection([
                LotteryTimedPair(
                    Lottery(1, c(8), c(4), [50], 50, 50, Maze('40_40_1', 147, 2, 169, 314)),
                    Lottery(2, c(8), c(4), [50], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
                ),
                LotteryTimedPair(
                    Lottery(3, c(8), c(4), [50], 80, 20, Maze('40_40_1', 147, 2, 169, 314)),
                    Lottery(4, c(8), c(4), [50], 80, 20, Maze('60_40_1', 147, 2, 169, 314))
                ),
                LotteryTimedPair(
                    Lottery(5, c(8), c(4), [40, 60], 80, 20, Maze('40_40_1', 147, 2, 169, 314)),
                    Lottery(6, c(10), c(2), [50], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
                ),
                LotteryTimedPair(
                    Lottery(7, c(10.44), c(2), [30], 60, 40, Maze('40_40_1', 147, 2, 169, 314)),
                    Lottery(8, c(8), c(4), [80], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
                ),
            ])
            player.participant.vars['timed_lottery_collection'] = lottery_pairs


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    left_lottery_id = models.IntegerField()
    right_lottery_id = models.IntegerField()
    left_lottery_time = models.IntegerField()
    right_lottery_time = models.IntegerField()
