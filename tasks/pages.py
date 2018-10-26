from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class TaskOne(Page):
    form_model = 'player'
    form_fields = ['task_one_choice']


page_sequence = [Instructions, TaskOne]
