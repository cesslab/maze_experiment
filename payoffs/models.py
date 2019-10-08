import random
from typing import List

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from experiment.lottery import Lottery
from experiment.mazes import Maze

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'payoffs'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    p1_chosen_lottery = models.IntegerField()
    p1_payoff = models.CurrencyField()
    p1_won_high_prize = models.BooleanField()
    p1_won_low_prize = models.BooleanField()
    solved_maze = models.BooleanField()

    def set_phase_one_payoff(self):
        random_round = self.participant.vars['preferred_pair_id']
        pair: List[Lottery] = self.participant.vars['preferred_lotteries'][random_round - 1]

        chosen_lottery_side = self.participant.vars["phase_1_chosen_lottery_side"]
        chosen_lottery: Lottery = pair[chosen_lottery_side]

        self.p1_chosen_lottery = chosen_lottery.id_number
        chosen_maze: Maze = chosen_lottery.maze

        self.solved_maze = chosen_maze.solved

        r = random.randint(0, 100)
        if chosen_maze.solved:
            if r <= chosen_lottery.prob_completed:
                self.p1_won_high_prize = True
                self.p1_payoff = chosen_lottery.high_prize
            else:
                self.p1_won_low_prize = True
                self.p1_payoff = chosen_lottery.low_prize
        else:
            if r <= chosen_lottery.prob_incomplete:
                self.p1_won_high_prize = True
                self.p1_payoff = chosen_lottery.high_prize
            else:
                self.p1_won_low_prize = True
                self.p1_payoff = chosen_lottery.low_prize
