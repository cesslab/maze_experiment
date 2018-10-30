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
                [[10, c(2.00), 90, c(1.60)], [10, c(3.85), 90, c(.10)]],
                [[20, c(2.00), 80, c(1.60)], [20, c(3.85), 80, c(.10)]],
                [[30, c(2.00), 70, c(1.60)], [30, c(3.85), 70, c(.10)]],
                [[40, c(2.00), 60, c(1.60)], [40, c(3.85), 60, c(.10)]],
                [[50, c(2.00), 50, c(1.60)], [50, c(3.85), 50, c(.10)]],
                [[60, c(2.00), 40, c(1.60)], [60, c(3.85), 40, c(.10)]],
                [[70, c(2.00), 30, c(1.60)], [70, c(3.85), 30, c(.10)]],
                [[80, c(2.00), 20, c(1.60)], [80, c(3.85), 20, c(.10)]],
                [[90, c(2.00), 10, c(1.60)], [90, c(3.85), 10, c(.10)]],
                [[100, c(2.00), 0, c(1.60)], [90, c(3.85), 10, c(.10)]],
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
            'cases': [c(.75), c(1), c(1.25), c(1.50), c(1.75), c(2), c(2.25), c(2.5), c(2.75), c(3)],
        }


class TaskFour(Page):
    form_model = 'player'
    form_fields = [
        'task_four_1', 'task_four_2', 'task_four_3', 'task_four_4', 'task_four_5',
        'task_four_6', 'task_four_7', 'task_four_8', 'task_four_9', 'task_four_10',
        'task_four_bet',
    ]

    def vars_for_template(self):
        return {
            'cases': [c(.75), c(1), c(1.25), c(1.50), c(1.75), c(2), c(2.25), c(2.50), c(2.75), c(3)],
        }


class TaskFive(Page):
    form_model = 'player'
    form_fields = ['task_five_invested']


class TaskSix(Page):
    form_model = 'player'
    form_fields = ['task_six_invested']


page_sequence = [Instructions, TaskOne, TaskTwo, TaskThree, TaskFour, TaskFive, TaskSix]
