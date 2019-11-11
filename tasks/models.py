from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer

from experiment.tasks import TaskTwo, TaskEight, TaskNine

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
                player.participant.vars['task_two'] = TaskTwo()
                player.participant.vars['task_eight'] = TaskEight()
                player.participant.vars['task_nine'] = TaskNine()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    task_one_choice = models.IntegerField(choices=[1, 2, 3], blank=False)
    task_two_1 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_2 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_3 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_4 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_5 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_6 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_7 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_8 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_9 = models.IntegerField(choices=[1, 2], blank=False)
    task_two_10 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_bet = models.IntegerField(choices=[1, 2], blank=False)
    task_three_1 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_2 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_3 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_4 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_5 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_6 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_7 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_8 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_9 = models.IntegerField(choices=[1, 2], blank=False)
    task_three_10 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_bet = models.IntegerField(choices=[1, 2], blank=False)
    task_four_1 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_2 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_3 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_4 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_5 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_6 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_7 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_8 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_9 = models.IntegerField(choices=[1, 2], blank=False)
    task_four_10 = models.IntegerField(choices=[1, 2], blank=False)
    task_eight_1 = models.IntegerField(choices=[1, 2], blank=False)
    task_eight_2 = models.IntegerField(choices=[1, 2], blank=False)
    task_eight_3 = models.IntegerField(choices=[1, 2], blank=False)
    task_eight_4 = models.IntegerField(choices=[1, 2], blank=False)
    task_eight_5 = models.IntegerField(choices=[1, 2], blank=False)
    task_eight_6 = models.IntegerField(choices=[1, 2], blank=False)
    task_eight_7 = models.IntegerField(choices=[1, 2], blank=False)
    task_eight_8 = models.IntegerField(choices=[1, 2], blank=False)
    task_eight_9 = models.IntegerField(choices=[1, 2], blank=False)
    task_eight_10 = models.IntegerField(choices=[1, 2], blank=False)
    task_eight_11 = models.IntegerField(choices=[1, 2], blank=False)
    task_nine_1 = models.IntegerField(choices=[1, 2], blank=False)
    task_nine_2 = models.IntegerField(choices=[1, 2], blank=False)
    task_nine_3 = models.IntegerField(choices=[1, 2], blank=False)
    task_nine_4 = models.IntegerField(choices=[1, 2], blank=False)
    task_nine_5 = models.IntegerField(choices=[1, 2], blank=False)
    task_nine_6 = models.IntegerField(choices=[1, 2], blank=False)
    task_nine_7 = models.IntegerField(choices=[1, 2], blank=False)
    task_nine_8 = models.IntegerField(choices=[1, 2], blank=False)
    task_nine_9 = models.IntegerField(choices=[1, 2], blank=False)
    task_nine_10 = models.IntegerField(choices=[1, 2], blank=False)
    task_nine_11 = models.IntegerField(choices=[1, 2], blank=False)
    task_five_invested = models.IntegerField(min=0, max=100, blank=False)
    task_six_invested = models.IntegerField(min=0, max=100, blank=False)
    distance = models.IntegerField(blank=False)
    # miles = 1, km = 2
    unit = models.IntegerField(choices=[1, 2], blank=False)
    percent = models.IntegerField(choices=[1, 2], blank=False)
