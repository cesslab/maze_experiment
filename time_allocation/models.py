from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer

from experiment.lottery import TimedLotteryPairCollection

author = 'Anwar A. Ruff'
doc = """Allocate Time to Lottery Mazes"""


class Constants(BaseConstants):
    name_in_url = 'time_allocation'
    players_per_group = None
    num_rounds = 8


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.participant.vars['time_lottery_pair_collection'] = TimedLotteryPairCollection()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    left_lottery_id = models.IntegerField(blank=False)
    right_lottery_id = models.IntegerField(blank=False)
    left_lottery_time = models.IntegerField(blank=False)
    right_lottery_time = models.IntegerField(blank=False)
