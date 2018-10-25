import random

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'time_allocation'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            lotteries = player.participant.vars['lotteries']
            random.shuffle(lotteries)
            for pair in lotteries:
                random.shuffle(pair)
            player.participant.vars['lotteries'] = lotteries


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    left_lottery_time = models.IntegerField()
    left_lottery_id = models.IntegerField()
    right_lottery_time = models.IntegerField()
    right_lottery_id = models.IntegerField()
