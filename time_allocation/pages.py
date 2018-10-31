from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from experiment.lottery import Lottery


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class TimeAllocationPage(Page):
    form_model = 'player'
    form_fields = ['left_lottery_time', 'right_lottery_time']

    def vars_for_template(self):
        lottery_pair = self.participant.vars['timed_lotteries'][self.round_number - 1]
        return {
            'l': lottery_pair[0],
            'r': lottery_pair[1],
            'max_time_seconds': self.session.config['max_time_seconds'],
        }

    def before_next_page(self):
        lottery_pair = self.participant.vars['timed_lotteries'][self.round_number - 1]
        left_lottery: Lottery = lottery_pair[0]
        right_lottery: Lottery = lottery_pair[1]

        self.player.left_lottery_id = left_lottery.id_number
        self.player.right_lottery_id = right_lottery.id_number

        left_lottery.time_limit = self.player.left_lottery_time
        right_lottery.time_limit = self.player.right_lottery_time

    def error_message(self, values):
        max_time = self.session.config['max_time_seconds']
        left = values['left_lottery_time']
        right = values['right_lottery_time']
        if left == "" or right == "":
            return "Time allocation, in seconds, is required for both V and W."

        left_val = int(left)
        right_val = int(right)
        if left_val + right_val != max_time:
            print("Error: Invalid time allocation - {}".format)
            return "The time in seconds for V and W must add up to exactly {}".format(max_time)


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [Instructions, TimeAllocationPage]
