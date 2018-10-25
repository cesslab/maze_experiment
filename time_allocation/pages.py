from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class TimeAllocationPage(Page):
    form_model = 'player'
    form_fields = ['left_lottery_id', 'left_lottery_time', 'right_lottery_time', 'right_lottery_time']

    def vars_for_template(self):
        lottery_pair = self.participant.vars['lotteries'][self.round_number - 1]
        return {
            'l': lottery_pair[0],
            'r': lottery_pair[1],
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [TimeAllocationPage]
