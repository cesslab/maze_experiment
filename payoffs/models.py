from otree.api import BaseConstants, BaseSubsession, BaseGroup, BasePlayer, models

author = 'Anwar A. Ruff'
doc = """Payoffs"""


class Constants(BaseConstants):
    name_in_url = 'payoffs'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    part_1_selected_lottery_pair_round_number = models.IntegerField()
    part_1_selected_lottery_id = models.IntegerField()
    part_1_selected_lottery_maze_solved = models.BooleanField()
    part_1_random_value = models.IntegerField()
    part_2_selected_lottery_pair_round_number = models.IntegerField()
    part_2_left_maze_solved = models.BooleanField()
    part_2_left_random_value = models.IntegerField()
    part_2_right_maze_solved = models.BooleanField()
    part_2_right_random_value = models.IntegerField()
    part_3_payoff_task_number = models.IntegerField()
    part_3_task_epsilon_payoff_case = models.IntegerField()
    part_3_task_epsilon_option_selected = models.IntegerField()
    part_3_task_epsilon_option_random_number = models.IntegerField()

