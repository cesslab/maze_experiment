from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer

from experiment.tasks import TaskAlpha, TaskBeta, TaskEpsilon

author = 'Anwar A. Ruff'
doc = """Tasks"""


class Constants(BaseConstants):
    name_in_url = 'tasks'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                player.participant.vars['task_alpha_a'] = TaskAlpha()
                player.participant.vars['task_alpha_b'] = TaskAlpha()
                player.participant.vars['task_alpha_c'] = TaskAlpha()
                player.participant.vars['task_beta_a'] = TaskBeta()
                player.participant.vars['task_beta_b'] = TaskBeta()
                player.participant.vars['task_epsilon'] = TaskEpsilon()




class Group(BaseGroup):
    pass


class Player(BasePlayer):
    task_alpha_a_1 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_a_2 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_a_3 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_a_4 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_a_5 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_a_6 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_a_7 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_a_8 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_a_9 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_a_10 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_a_11 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_b_1 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_b_2 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_b_3 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_b_4 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_b_5 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_b_6 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_b_7 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_b_8 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_b_9 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_b_10 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_b_11 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_c_1 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_c_2 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_c_3 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_c_4 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_c_5 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_c_6 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_c_7 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_c_8 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_c_9 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_c_10 = models.IntegerField(choices=[1, 2], blank=False)
    task_alpha_c_11 = models.IntegerField(choices=[1, 2], blank=False)

    task_beta_a_1 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_a_2 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_a_3 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_a_4 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_a_5 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_a_6 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_a_7 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_a_8 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_a_9 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_a_10 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_a_11 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_b_1 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_b_2 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_b_3 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_b_4 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_b_5 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_b_6 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_b_7 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_b_8 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_b_9 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_b_10 = models.IntegerField(choices=[1, 2], blank=False)
    task_beta_b_11 = models.IntegerField(choices=[1, 2], blank=False)

    task_gamma_1 = models.IntegerField(label="$2 for sure and a lottery giving you a p% chance of getting $12 and a (1-p%) chance of getting $0. Enter a percent chance between 0% and 100%", min=0, max=100, blank=False)
    task_gamma_2 = models.IntegerField(label="$4 for sure and a lottery giving you a p% chance of getting $12 and a (1-p%) chance of getting $0. Enter a percent chance between 0% and 100%", min=0, max=100, blank=False)
    task_gamma_3 = models.IntegerField(label="$8 for sure and a lottery giving you a p% chance of getting $12 and a (1-p%) chance of getting $0. Enter a percent chance between 0% and 100%", min=0, max=100, blank=False)
    task_gamma_4 = models.IntegerField(label="$10 for sure and a lottery giving you a p% chance of getting $12 and a (1-p%) chance of getting $0. Enter a percent chance between 0% and 100%", min=0, max=100, blank=False)

    task_delta_choice = models.IntegerField(choices=[1, 2, 3], blank=False)

    task_epsilon_1 = models.IntegerField(choices=[1, 2], blank=False)
    task_epsilon_2 = models.IntegerField(choices=[1, 2], blank=False)
    task_epsilon_3 = models.IntegerField(choices=[1, 2], blank=False)
    task_epsilon_4 = models.IntegerField(choices=[1, 2], blank=False)
    task_epsilon_5 = models.IntegerField(choices=[1, 2], blank=False)
    task_epsilon_6 = models.IntegerField(choices=[1, 2], blank=False)
    task_epsilon_7 = models.IntegerField(choices=[1, 2], blank=False)
    task_epsilon_8 = models.IntegerField(choices=[1, 2], blank=False)
    task_epsilon_9 = models.IntegerField(choices=[1, 2], blank=False)
    task_epsilon_10 = models.IntegerField(choices=[1, 2], blank=False)

    task_zeta_distance = models.IntegerField(blank=False)
    # miles = 1, km = 2
    task_zeta_unit = models.IntegerField(choices=[1, 2], blank=False)
    task_zeta_percent = models.IntegerField(min=0, max=100, blank=False)

    task_eta_invested = models.IntegerField(min=0, max=100, blank=False)

    task_theta_invested = models.IntegerField(min=0, max=100, blank=False)

    # task_seven_1 = models.IntegerField(choices=[1, 2], blank=False)
    # task_seven_2 = models.IntegerField(choices=[1, 2], blank=False)
    # task_seven_3 = models.IntegerField(choices=[1, 2], blank=False)
    # task_seven_4 = models.IntegerField(choices=[1, 2], blank=False)
    # task_seven_5 = models.IntegerField(choices=[1, 2], blank=False)
    # task_seven_6 = models.IntegerField(choices=[1, 2], blank=False)
    # task_seven_7 = models.IntegerField(choices=[1, 2], blank=False)
    # task_seven_8 = models.IntegerField(choices=[1, 2], blank=False)
    # task_seven_9 = models.IntegerField(choices=[1, 2], blank=False)
    # task_seven_10 = models.IntegerField(choices=[1, 2], blank=False)
    # task_three_bet = models.IntegerField(choices=[1, 2], blank=False)
    # task_three_1 = models.IntegerField(choices=[1, 2], blank=False)
    # task_three_2 = models.IntegerField(choices=[1, 2], blank=False)
    # task_three_3 = models.IntegerField(choices=[1, 2], blank=False)
    # task_three_4 = models.IntegerField(choices=[1, 2], blank=False)
    # task_three_5 = models.IntegerField(choices=[1, 2], blank=False)
    # task_three_6 = models.IntegerField(choices=[1, 2], blank=False)
    # task_three_7 = models.IntegerField(choices=[1, 2], blank=False)
    # task_three_8 = models.IntegerField(choices=[1, 2], blank=False)
    # task_three_9 = models.IntegerField(choices=[1, 2], blank=False)
    # task_three_10 = models.IntegerField(choices=[1, 2], blank=False)
    # task_four_bet = models.IntegerField(choices=[1, 2], blank=False)
    # task_four_1 = models.IntegerField(choices=[1, 2], blank=False)
    # task_four_2 = models.IntegerField(choices=[1, 2], blank=False)
    # task_four_3 = models.IntegerField(choices=[1, 2], blank=False)
    # task_four_4 = models.IntegerField(choices=[1, 2], blank=False)
    # task_four_5 = models.IntegerField(choices=[1, 2], blank=False)
    # task_four_6 = models.IntegerField(choices=[1, 2], blank=False)
    # task_four_7 = models.IntegerField(choices=[1, 2], blank=False)
    # task_four_8 = models.IntegerField(choices=[1, 2], blank=False)
    # task_four_9 = models.IntegerField(choices=[1, 2], blank=False)
    # task_four_10 = models.IntegerField(choices=[1, 2], blank=False)
    # task_eight_1 = models.IntegerField(choices=[1, 2], blank=False)
    # task_eight_2 = models.IntegerField(choices=[1, 2], blank=False)
    # task_eight_3 = models.IntegerField(choices=[1, 2], blank=False)
    # task_eight_4 = models.IntegerField(choices=[1, 2], blank=False)
    # task_eight_5 = models.IntegerField(choices=[1, 2], blank=False)
    # task_eight_6 = models.IntegerField(choices=[1, 2], blank=False)
    # task_eight_7 = models.IntegerField(choices=[1, 2], blank=False)
    # task_eight_8 = models.IntegerField(choices=[1, 2], blank=False)
    # task_eight_9 = models.IntegerField(choices=[1, 2], blank=False)
    # task_eight_10 = models.IntegerField(choices=[1, 2], blank=False)
    # task_eight_11 = models.IntegerField(choices=[1, 2], blank=False)
    # task_nine_1 = models.IntegerField(choices=[1, 2], blank=False)
    # task_nine_2 = models.IntegerField(choices=[1, 2], blank=False)
    # task_nine_3 = models.IntegerField(choices=[1, 2], blank=False)
    # task_nine_4 = models.IntegerField(choices=[1, 2], blank=False)
    # task_nine_5 = models.IntegerField(choices=[1, 2], blank=False)
    # task_nine_6 = models.IntegerField(choices=[1, 2], blank=False)
    # task_nine_7 = models.IntegerField(choices=[1, 2], blank=False)
    # task_nine_8 = models.IntegerField(choices=[1, 2], blank=False)
    # task_nine_9 = models.IntegerField(choices=[1, 2], blank=False)
    # task_nine_10 = models.IntegerField(choices=[1, 2], blank=False)
    # task_nine_11 = models.IntegerField(choices=[1, 2], blank=False)
    # task_five_invested = models.IntegerField(min=0, max=100, blank=False)
