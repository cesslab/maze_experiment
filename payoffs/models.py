from typing import List

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from experiment.lottery import Lottery
from experiment.mazes import Maze

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'payoffs'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    phase_one_left_lottery = models.IntegerField()
    phase_one_right_lottery = models.IntegerField()
    phase_one_payoff = models.CurrencyField()

    def set_phase_one_payoff(self):
        pair: List[Lottery] = self.participant.vars['rand_pair_phase_1']
        left_maze: Maze = pair[0].maze

