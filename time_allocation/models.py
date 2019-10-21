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
    num_rounds = 7


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.participant.vars['time_lottery_pair_collection'] = TimedLotteryPairCollection()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    left_lottery_id = models.IntegerField()
    right_lottery_id = models.IntegerField()
    left_lottery_time = models.IntegerField()
    right_lottery_time = models.IntegerField()
