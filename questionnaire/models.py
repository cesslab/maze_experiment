from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Anwar A. Ruff'

doc = """
Questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.StringField()
    age = models.IntegerField(min=18, max=100)
    major = models.StringField()
    year_in_college = models.IntegerField(min=0, max=10)
    q1 = models.LongStringField()
    q2 = models.LongStringField()
    q3 = models.LongStringField()
    q4 = models.LongStringField()
    q5 = models.LongStringField()
    q6 = models.LongStringField()
    q7 = models.LongStringField()
