from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from experiment.tasks import TaskTwo


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class TaskOne(Page):
    form_model = 'player'
    form_fields = ['task_one_choice']


class TaskTwoPage(Page):
    form_model = 'player'
    form_fields = [
        'task_two_1', 'task_two_2', 'task_two_3', 'task_two_4', 'task_two_5',
        'task_two_6', 'task_two_7', 'task_two_8', 'task_two_9', 'task_two_10',
    ]

    def vars_for_template(self):
        task_two: TaskTwo = self.participant.vars['task_two']
        return {
            'cases': task_two.cases
        }

    def before_next_page(self):
        task_two: TaskTwo = self.participant.vars['task_two']
        entered_options = [
            self.player.task_two_1, self.player.task_two_2, self.player.task_two_3, self.player.task_two_3,
            self.player.task_two_4, self.player.task_two_5, self.player.task_two_6, self.player.task_two_7,
            self.player.task_two_8, self.player.task_two_9, self.player.task_two_10
        ]

        payoff_case_number = task_two.payoff_case_number
        task_two.payoff_option = entered_options[payoff_case_number - 1]

        self.player.payoff = task_two.payoff_option.payoff
        print("Task 2 Payoff {}".format(self.player.payoff))




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


class TaskSeven(Page):
    form_model = 'player'
    form_fields = ['distance', 'unit']


page_sequence = [Instructions, TaskOne, TaskTwoPage, TaskThree, TaskFour, TaskFive, TaskSix, TaskSeven]
