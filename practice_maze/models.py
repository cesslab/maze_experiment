from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer

author = 'Anwar A. Ruff'
doc = """Practice Maze"""


class Constants(BaseConstants):
    name_in_url = 'practice_maze'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    maze_id = models.CharField(max_length=255, blank=False)
    solved = models.IntegerField(choices=[0, 1], default=0, blank=False)
    solve_time_seconds = models.IntegerField(blank=False)

