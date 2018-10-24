from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


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
        self.player.left_lottery_id = lottery_pair[0].id_number
        self.player.right_lottery_id = lottery_pair[1].id_number


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    ChoicePage,
]
