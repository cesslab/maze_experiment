from otree.api import Currency as c
from ._builtin import Page

from experiment.tasks import TaskTwo, TaskEight, TaskNine


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class TaskFourPage(Page):
    form_model = 'player'
    form_fields = ['task_four_choice']


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


class TaskEightPage(Page):
    form_model = 'player'
    form_fields = [
        'task_eight_1', 'task_eight_2', 'task_eight_3', 'task_eight_4', 'task_eight_5',
        'task_eight_6', 'task_eight_7', 'task_eight_8', 'task_eight_9', 'task_eight_10', 'task_eight_11'
    ]

    def vars_for_template(self):
        task_eight: TaskEight = self.participant.vars['task_eight']
        return {
            'cases': task_eight.cases
        }

    def before_next_page(self):
        task_eight: TaskTwo = self.participant.vars['task_eight']
        entered_options = [
            self.player.task_eight_1, self.player.task_eight_2, self.player.task_eight_3, self.player.task_eight_3,
            self.player.task_eight_4, self.player.task_eight_5, self.player.task_eight_6, self.player.task_eight_7,
            self.player.task_eight_8, self.player.task_eight_9, self.player.task_eight_10, self.player.task_eight_11
        ]

        payoff_case_number = task_eight.payoff_case_number
        task_eight.payoff_option = entered_options[payoff_case_number - 1]

        self.player.payoff = task_eight.payoff_option.payoff


class TaskNinePage(Page):
    form_model = 'player'
    form_fields = [
        'task_nine_1', 'task_nine_2', 'task_nine_3', 'task_nine_4', 'task_nine_5',
        'task_nine_6', 'task_nine_7', 'task_nine_8', 'task_nine_9', 'task_nine_10', 'task_nine_11'
    ]

    def vars_for_template(self):
        task_nine: TaskNine = self.participant.vars['task_nine']
        return {
            'cases': task_nine.cases
        }

    def before_next_page(self):
        task_nine: TaskTwo = self.participant.vars['task_nine']
        entered_options = [
            self.player.task_nine_1, self.player.task_nine_2, self.player.task_nine_3, self.player.task_nine_3,
            self.player.task_nine_4, self.player.task_nine_5, self.player.task_nine_6, self.player.task_nine_7,
            self.player.task_nine_8, self.player.task_nine_9, self.player.task_nine_10, self.player.task_nine_11
        ]

        payoff_case_number = task_nine.payoff_case_number
        task_nine.payoff_option = entered_options[payoff_case_number - 1]

        self.player.payoff = task_nine.payoff_option.payoff


class TaskThreePage(Page):
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


class _TaskFourPage(Page):
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


class TaskFivePage(Page):
    form_model = 'player'
    form_fields = ['task_five_invested']


class TaskSixPage(Page):
    form_model = 'player'
    form_fields = ['task_six_invested']


class TaskSevenPage(Page):
    form_model = 'player'
    form_fields = ['distance', 'unit']


page_sequence = [Instructions, TaskOnePage, TaskTwoPage, TaskThreePage, _TaskFourPage, TaskFivePage, TaskSixPage, TaskSevenPage, TaskEightPage, TaskNinePage]
