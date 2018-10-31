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
        lottery_pair = self.participant.vars['lotteries'][self.round_number - 1]
        return {
            'l': lottery_pair[0],
            'r': lottery_pair[1],
        }

    def before_next_page(self):
        lottery_pair = self.participant.vars['lotteries'][self.round_number - 1]
        left_lottery: Lottery = lottery_pair[0]
        right_lottery: Lottery = lottery_pair[1]

        self.player.left_lottery_id = left_lottery.id_number
        self.player.right_lottery_id = right_lottery.id_number

        player_preference = self.player.preference

        left = 1
        either = 2
        right = 3
        if player_preference == either:
            player_preference = random.choice(left, right)

        if player_preference == left:
            self.player.chosen_lottery = left_lottery.id_number
            left_lottery.is_preference = True
        else:
            self.player.chosen_lottery = right_lottery.id_number
            right_lottery.is_preference = True


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [Instructions, ChoicePage]
