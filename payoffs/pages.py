from typing import List
from ._builtin import Page, WaitPage

from experiment.lottery import Lottery
from .models import Player


class Instructions(Page):
    def before_next_page(self):
        self.player.set_phase_one_payoff()


class Payoffs(Page):
    def vars_for_template(self):
        random_round = self.player.participant.vars['preferred_pair_id']
        pair: List[Lottery] = self.player.participant.vars['preferred_lotteries'][random_round - 1]

        chosen_lottery_side = self.player.participant.vars["preferred_lottery"]
        chosen_lottery: Lottery = pair[chosen_lottery_side]
        if chosen_lottery_side == 0:
            lottery_label = 'V'
        else:
            lottery_label = 'W'

        return {
            'l': chosen_lottery,
            'lottery_label': lottery_label,
            'random_round': random_round,
            'won_low': self.player.p1_won_low_prize,
            'won_high': self.player.p1_won_high_prize,
            'payoff': self.player.p1_payoff,
            'solved_maze': self.player.solved_maze,
        }


page_sequence = [
    Instructions,
    Payoffs
]
