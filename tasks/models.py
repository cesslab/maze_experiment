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

    task_gamma_1 = models.IntegerField(label="$2 for sure and a lottery giving you a p% chance of getting $12 and a (100%-p%) chance of getting $0. Enter a percent chance between 0% and 100%", min=0, max=100, blank=False)
    task_gamma_2 = models.IntegerField(label="$4 for sure and a lottery giving you a p% chance of getting $12 and a (100%-p%) chance of getting $0. Enter a percent chance between 0% and 100%", min=0, max=100, blank=False)
    task_gamma_3 = models.IntegerField(label="$8 for sure and a lottery giving you a p% chance of getting $12 and a (100%-p%) chance of getting $0. Enter a percent chance between 0% and 100%", min=0, max=100, blank=False)
    task_gamma_4 = models.IntegerField(label="$10 for sure and a lottery giving you a p% chance of getting $12 and a (100%-p%) chance of getting $0. Enter a percent chance between 0% and 100%", min=0, max=100, blank=False)

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

    pass_code = models.IntegerField(blank=True)
