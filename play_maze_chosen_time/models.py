from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer

author = 'Anwar A. Ruff'
doc = """Chosen Time Maze Play"""

class Constants(BaseConstants):
    name_in_url = 'play_maze_chosen_time'
    players_per_group = None
    # The number of rounds equal the number of pairs of lotteries displayed in the time allocation phase
    num_rounds = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    maze_id = models.CharField(max_length=255, blank=False)
    solved = models.IntegerField(choices=[0, 1], default=0, blank=False)
    solve_time_seconds = models.IntegerField(blank=False)
    lottery_id = models.IntegerField(blank=False)

