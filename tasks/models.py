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
    name_in_url = 'tasks'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    task_one_choice = models.IntegerField(choices=[1, 2, 3], blank=False)
    task_two_1 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_2 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_3 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_4 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_5 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_6 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_7 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_8 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_9 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_10 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_bet = models.IntegerField(choices=[1, 2], blank=False)
    task_three_1 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_2 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_3 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_4 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_5 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_6 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_7 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_8 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_9 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_10 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_bet = models.IntegerField(choices=[1, 2], blank=False)
    task_four_1 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_2 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_3 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_4 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_5 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_6 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_7 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_8 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_9 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_10 = models.IntegerField(choices=[1, 2], blank=False)
    task_five_invested = models.IntegerField(min=0, max=100, blank=False)
    task_six_invested = models.IntegerField(min=0, max=100, blank=False)
