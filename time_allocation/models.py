import random

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from experiment.lottery import Lottery
from experiment.mazes import Maze

class Constants(BaseConstants):
    name_in_url = 'time_allocation'
    players_per_group = None
    num_rounds = 4


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            lotteries = [
                [
                    Lottery(1, c(8), c(4), [50], 50, 50, Maze('easy1', 147, 2, 169, 314)),
                    Lottery(2, c(8), c(4), [50], 60, 40, Maze('easy2', 147, 2, 169, 314))
                ],
                [
                    Lottery(3, c(8), c(4), [50], 80, 20, Maze('easy3', 147, 2, 169, 314)),
                    Lottery(4, c(8), c(4), [50], 80, 20, Maze('easyM1', 147, 2, 169, 314))
                ],
                [
                    Lottery(5, c(8), c(4), [40, 60], 80, 20, Maze('easyM2', 147, 2, 169, 314)),
                    Lottery(6, c(10), c(2), [50], 60, 40, Maze('easyM3', 147, 2, 169, 314))
                ],
                [
                    Lottery(7, c(10.44), c(2), [30], 60, 40, Maze('hard1', 147, 2, 169, 314)),
                    Lottery(8, c(8), c(4), [80], 60, 40, Maze('hard2', 147, 2, 169, 314))
                ],
            ]
            random.shuffle(lotteries)
            for pair in lotteries:
                random.shuffle(pair)
            player.participant.vars['timed_lotteries'] = lotteries
            player.participant.vars['rand_pair_phase_2'] = random.randint(0, 3)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    left_lottery_time = models.IntegerField()
    left_lottery_id = models.IntegerField()
    right_lottery_time = models.IntegerField()
    right_lottery_id = models.IntegerField()
