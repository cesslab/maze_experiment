from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class TaskOne(Page):
    form_model = 'player'
    form_fields = ['task_one_choice']


class TaskTwo(Page):
    form_model = 'player'
    form_fields = [
        'task_two_1', 'task_two_2', 'task_two_3', 'task_two_4', 'task_two_5',
        'task_two_6', 'task_two_7', 'task_two_8', 'task_two_9', 'task_two_10',
    ]

    def vars_for_template(self):
        return {
            'cases': [
                [[10, 200, 90, 160], [10, 385, 90, 10]],
                [[20, 200, 80, 160], [20, 385, 80, 10]],
                [[30, 200, 70, 160], [30, 385, 70, 10]],
                [[40, 200, 60, 160], [40, 385, 60, 10]],
                [[50, 200, 50, 160], [50, 385, 50, 10]],
                [[60, 200, 40, 160], [60, 385, 40, 10]],
                [[70, 200, 30, 160], [70, 385, 30, 10]],
                [[80, 200, 20, 160], [80, 385, 20, 10]],
                [[90, 200, 10, 160], [90, 385, 10, 10]],
                [[100, 200, 0, 160], [90, 385, 10, 10]],
            ],
        }

class TaskThree(Page):
    form_model = 'player'
    form_fields = [
        'task_three_1', 'task_three_2', 'task_three_3', 'task_three_4', 'task_three_5',
        'task_three_6', 'task_three_7', 'task_three_8', 'task_three_9', 'task_three_10',
        'task_three_bet',
    ]

    def vars_for_template(self):
        return {
            'b_options': [75, 100, 125, 150, 175, 200, 225, 250, 275, 300],
        }



page_sequence = [Instructions, TaskOne, TaskTwo]
