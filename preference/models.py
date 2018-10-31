import random

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from experiment.lottery import Lottery
from experiment.mazes import Maze


class Constants(BaseConstants):
    name_in_url = 'preference'
    players_per_group = None
    num_rounds = 4


class Subsession(BaseSubsession):
    def creating_session(self):

        for player in self.get_players():
            lotteries = [
                [
                    Lottery(1, c(8), c(4), [.5], .5, .5, Maze('easy1', 147, 2, 169, 314)),
                    Lottery(2, c(8), c(4), [.5], .6, .4, Maze('easy2', 147, 2, 169, 314))
                ],
                [
                    Lottery(3, c(8), c(4), [.5], .8, .2, Maze('easy3', 147, 2, 169, 314)),
                    Lottery(4, c(8), c(4), [.5], .8, .2, Maze('easyM1', 147, 2, 169, 314))
                ],
                [
                    Lottery(5, c(8), c(4), [.4, .6], .8, .2, Maze('easyM2', 147, 2, 169, 314)),
                    Lottery(6, c(10), c(2), [.5], .6, .4, Maze('easyM3', 147, 2, 169, 314))
                ],
                [
                    Lottery(7, c(10.44), c(2), [.3], .6, .4, Maze('hard1', 147, 2, 169, 314)),
                    Lottery(8, c(8), c(4), [.8], .6, .4, Maze('hard2', 147, 2, 169, 314))
                ],
            ]
            random.shuffle(lotteries)
            for pair in lotteries:
                random.shuffle(pair)
            player.participant.vars['preferred_lotteries'] = lotteries


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    left_lottery_id = models.IntegerField()
    right_lottery_id = models.IntegerField()
    preference = models.IntegerField()
    chosen_lottery = models.BooleanField(default=False)
