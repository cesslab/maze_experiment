import random

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from experiment.lottery import Lottery, LotteryPreferencePair, PreferredLotteryPairCollection
from experiment.mazes import Maze


class Constants(BaseConstants):
    name_in_url = 'preference'
    players_per_group = None
    num_rounds = 4


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                preferred_lottery_pair_collection = PreferredLotteryPairCollection([
                    LotteryPreferencePair(
                        Lottery(1, c(8), c(4), [50], 50, 50, Maze('40_40_1', 147, 2, 169, 314)),
                        Lottery(2, c(8), c(4), [50], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
                    ),
                    LotteryPreferencePair(
                        Lottery(3, c(8), c(4), [50], 80, 20, Maze('40_40_1', 147, 2, 169, 314)),
                        Lottery(4, c(8), c(4), [50], 80, 20, Maze('60_40_1', 147, 2, 169, 314))
                    ),
                    LotteryPreferencePair(
                        Lottery(5, c(8), c(4), [40, 60], 80, 20, Maze('40_40_1', 147, 2, 169, 314)),
                        Lottery(6, c(10), c(2), [50], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
                    ),
                    LotteryPreferencePair(
                        Lottery(7, c(10.44), c(2), [30], 60, 40, Maze('40_40_1', 147, 2, 169, 314)),
                        Lottery(8, c(8), c(4), [80], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
                    ),
                ])
                player.participant.vars['preferred_lottery_pair_collection'] = preferred_lottery_pair_collection


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    left_lottery_id = models.IntegerField(default=False)
    right_lottery_id = models.IntegerField(default=False)
    preference = models.IntegerField(default=False)
