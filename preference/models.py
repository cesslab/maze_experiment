import random

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from experiment.lottery import Lottery


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'preference'
    players_per_group = None
    num_rounds = 4


class Subsession(BaseSubsession):
    def creating_session(self):

        for player in self.get_players():
            lotteries = [
                [Lottery(1, 800, 400, [.5], .5, .5), Lottery(2, 800, 400, [.5], .6, .4)],
                [Lottery(3, 800, 400, [.5], .8, .2), Lottery(4, 800, 400, [.5], .8, .2)],
                [Lottery(5, 800, 400, [.4, .6], .8, .2), Lottery(6, 1000, 200, [.5], .6, .4)],
                [Lottery(7, 1044, 200, [.3], .6, .4), Lottery(8, 800, 400, [.8], .6, .4)],
            ]
            random.shuffle(lotteries)
            for pair in lotteries:
                random.shuffle(pair)
            player.participant.vars['lotteries'] = lotteries


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    left_lottery_id = models.IntegerField()
    right_lottery_id = models.IntegerField()
    preference = models.IntegerField()
