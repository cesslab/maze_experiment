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
                player.participant.vars['preferred_lottery_pair_collection'] = PreferredLotteryPairCollection()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    left_lottery_id = models.IntegerField(default=False)
    right_lottery_id = models.IntegerField(default=False)
    preference = models.IntegerField(default=False)
