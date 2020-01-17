from otree.api import Currency as c
from ._builtin import Page

from experiment.tasks import TaskAlpha, TaskBeta, TaskEpsilon


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class TaskAlphaPage(Page):
    form_model = 'player'
    form_fields = [
        'task_alpha_a_1', 'task_alpha_a_2', 'task_alpha_a_3', 'task_alpha_a_4', 'task_alpha_a_5',
        'task_alpha_a_6', 'task_alpha_a_7', 'task_alpha_a_8', 'task_alpha_a_9', 'task_alpha_a_10', 'task_alpha_a_11',
        'task_alpha_b_1', 'task_alpha_b_2', 'task_alpha_b_3', 'task_alpha_b_4', 'task_alpha_b_5',
        'task_alpha_b_6', 'task_alpha_b_7', 'task_alpha_b_8', 'task_alpha_b_9', 'task_alpha_b_10', 'task_alpha_b_11',
        'task_alpha_c_1', 'task_alpha_c_2', 'task_alpha_c_3', 'task_alpha_c_4', 'task_alpha_c_5',
        'task_alpha_c_6', 'task_alpha_c_7', 'task_alpha_c_8', 'task_alpha_c_9', 'task_alpha_c_10', 'task_alpha_c_11',
    ]

    def vars_for_template(self):
        task_alpha_a: TaskAlpha = self.participant.vars['task_alpha_a']
        task_alpha_b: TaskAlpha = self.participant.vars['task_alpha_b']
        task_alpha_c: TaskAlpha = self.participant.vars['task_alpha_c']
        return {
            'task_number': 1,
            'cases_one_a': task_alpha_a.cases,
            'cases_one_b': task_alpha_b.cases,
            'cases_one_c': task_alpha_c.cases,
            'a': [
                'task_alpha_a_1', 'task_alpha_a_2', 'task_alpha_a_3', 'task_alpha_a_4', 'task_alpha_a_5',
                'task_alpha_a_6', 'task_alpha_a_7', 'task_alpha_a_8', 'task_alpha_a_9', 'task_alpha_a_10', 'task_alpha_a_11',
            ],
            'b': [
                'task_alpha_b_1', 'task_alpha_b_2', 'task_alpha_b_3', 'task_alpha_b_4', 'task_alpha_b_5',
                'task_alpha_b_6', 'task_alpha_b_7', 'task_alpha_b_8', 'task_alpha_b_9', 'task_alpha_b_10', 'task_alpha_b_11',
            ],
            'c': [
                'task_alpha_c_1', 'task_alpha_c_2', 'task_alpha_c_3', 'task_alpha_c_4', 'task_alpha_c_5',
                'task_alpha_c_6', 'task_alpha_c_7', 'task_alpha_c_8', 'task_alpha_c_9', 'task_alpha_c_10', 'task_alpha_c_11',
            ]
        }

    def before_next_page(self):
        pass
        # task_nine: TaskNine = self.participant.vars['task_nine']
        # entered_options = [
        #     self.player.task_nine_1, self.player.task_nine_2, self.player.task_nine_3, self.player.task_nine_3,
        #     self.player.task_nine_4, self.player.task_nine_5, self.player.task_nine_6, self.player.task_nine_7,
        #     self.player.task_nine_8, self.player.task_nine_9, self.player.task_nine_10, self.player.task_nine_11
        # ]
        #
        # payoff_case_number = task_nine.payoff_case_number
        # task_nine.payoff_option = entered_options[payoff_case_number - 1]
        #
        # self.player.payoff = task_nine.payoff_option.payoff


class TaskBetaPage(Page):
    form_model = 'player'
    form_fields = [
        'task_beta_a_1', 'task_beta_a_2', 'task_beta_a_3', 'task_beta_a_4', 'task_beta_a_5',
        'task_beta_a_6', 'task_beta_a_7', 'task_beta_a_8', 'task_beta_a_9', 'task_beta_a_10', 'task_beta_a_11',
        'task_beta_b_1', 'task_beta_b_2', 'task_beta_b_3', 'task_beta_b_4', 'task_beta_b_5',
        'task_beta_b_6', 'task_beta_b_7', 'task_beta_b_8', 'task_beta_b_9', 'task_beta_b_10', 'task_beta_b_11',
    ]

    def vars_for_template(self):
        task_beta_a: TaskBeta = self.participant.vars['task_beta_a']
        task_beta_b: TaskBeta = self.participant.vars['task_beta_b']
        return {
            'task_number': 2,
            'cases_beta_a': task_beta_a.cases,
            'cases_beta_b': task_beta_b.cases,
            'high_a': c(8),
            'low_a': c(4),
            'high_b': c(8),
            'low_b': c(4),
        }


class TaskGammaPage(Page):
    form_model = 'player'
    form_fields = ['task_gamma_1', 'task_gamma_2', 'task_gamma_3', 'task_gamma_4']

    def vars_for_template(self):
        return {
            'task_number': 3,
        }


class TaskDeltaPage(Page):
    form_model = 'player'
    form_fields = ['task_delta_choice']

    def vars_for_template(self):
        return {
            'task_number': 4,
        }


class TaskEpsilonPage(Page):
    form_model = 'player'
    form_fields = [
        'task_epsilon_1', 'task_epsilon_2', 'task_epsilon_3', 'task_epsilon_4', 'task_epsilon_5',
        'task_epsilon_6', 'task_epsilon_7', 'task_epsilon_8', 'task_epsilon_9', 'task_epsilon_10',
    ]

    def vars_for_template(self):
        task_epsilon: TaskEpsilon = self.participant.vars['task_epsilon']
        return {
            'task_number': 5,
            'cases': task_epsilon.cases
        }

    def before_next_page(self):
        task_epsilon: TaskEpsilon = self.participant.vars['task_epsilon']
        entered_options = [
            self.player.task_epsilon_1, self.player.task_epsilon_2, self.player.task_epsilon_3, self.player.task_epsilon_3,
            self.player.task_epsilon_4, self.player.task_epsilon_5, self.player.task_epsilon_6, self.player.task_epsilon_7,
            self.player.task_epsilon_8, self.player.task_epsilon_9, self.player.task_epsilon_10
        ]

        self.participant.vars['payment_task_number'] = 5

        payoff_case_number = task_epsilon.payoff_case_number
        task_epsilon.payoff_option = entered_options[payoff_case_number - 1]

        self.player.payoff = task_epsilon.payoff_option.payoff


class TaskZetaPage(Page):
    form_model = 'player'
    form_fields = ['task_zeta_distance', 'task_zeta_unit', 'task_zeta_percent']

    def vars_for_template(self):
        return {
            'task_number': 6,
        }


class TaskEtaPage(Page):
    form_model = 'player'
    form_fields = ['task_eta_invested']

    def vars_for_template(self):
        return {
            'task_number': 7,
        }


class TaskThetaPage(Page):
    form_model = 'player'
    form_fields = ['task_theta_invested']

    def vars_for_template(self):
        return {
            'task_number': 8,
        }


page_sequence = [
    Instructions, TaskAlphaPage, TaskBetaPage, TaskGammaPage, TaskDeltaPage, TaskEpsilonPage, TaskZetaPage,
    TaskEtaPage, TaskThetaPage
]
