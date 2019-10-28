from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
from experiment.lottery import PreferredLotteryPairCollection

author = 'Anwar A. Ruff'
doc = """Chose Preferred Lotteries"""


class Constants(BaseConstants):
    name_in_url = 'preference'
    players_per_group = None
    num_rounds = 7


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                player.participant.vars['preferred_lottery_pair_collection'] = PreferredLotteryPairCollection()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    left_lottery_id = models.IntegerField(blank=False)
    right_lottery_id = models.IntegerField(blank=False)
    preference = models.IntegerField(blank=False)
