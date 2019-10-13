from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'play_maze_fixed_time'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    maze_id = models.CharField(max_length=255)
    solved = models.IntegerField(default=0)
    solve_time_seconds = models.IntegerField()

