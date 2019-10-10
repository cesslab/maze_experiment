import random

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from experiment.lottery import Lottery


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class ChoicePage(Page):
    form_model = 'player'
    form_fields = ['preference']

    def vars_for_template(self):
        lottery_pair = self.participant.vars['preferred_lottery_pairs'][self.round_number - 1]
        return {
            'l': lottery_pair[0],
            'r': lottery_pair[1],
        }

    def before_next_page(self):
        lottery_pair = self.participant.vars['preferred_lottery_pairs'][self.round_number - 1]
        left_lottery: Lottery = lottery_pair[0]
        right_lottery: Lottery = lottery_pair[1]

        self.player.left_lottery_id = left_lottery.id_number
        self.player.right_lottery_id = right_lottery.id_number

        player_preference = self.player.preference

        LEFT = 1
        EITHER = 2
        RIGHT = 3
        # Randomly choose the player preference if either was selected

        if self.player.preference == EITHER:
            self.player.realized_preference = random.choice([LEFT, RIGHT])
        else:
            self.player.realized_preference = self.player.preference

        if self.player.realized_preference == LEFT:
            self.player.chosen_lottery = left_lottery.id_number
            left_lottery.is_preference = True
            self.player.participant.vars["preferred_lottery"] = 0
        else:
            self.player.chosen_lottery = right_lottery.id_number
            right_lottery.is_preference = True
            self.player.participant.vars["preferred_lottery"] = 1


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [Instructions, ChoicePage]
