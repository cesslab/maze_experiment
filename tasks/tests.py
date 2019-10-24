import random

from ._builtin import Bot
from otree.api import expect, SubmissionMustFail

from .pages import TaskOne, TaskTwoPage, TaskThree, TaskFour, TaskFive, TaskSix, TaskSeven, Instructions
from experiment.tasks import TaskTwo


class PlayerBot(Bot):
    def play_round(self):
        yield (Instructions)

        # Test task 1
        SubmissionMustFail(TaskOne, {'task_one_choice': random.randint(4, 100)})
        yield(TaskOne, {'task_one_choice': random.choice([1, 2, 3])})

        # Test task 2
        incorrect_form_field_values = {
            'task_two_1': '', 'task_two_2': '', 'task_two_3': '', 'task_two_4': '', 'task_two_5': '',
            'task_two_6': '', 'task_two_7': '', 'task_two_8': '', 'task_two_9': '', 'task_two_10': ''
        }
        yield(SubmissionMustFail(TaskTwoPage, incorrect_form_field_values))

        correct_form_field_values = {
            'task_two_1': random.choice([1, 2]), 'task_two_2': random.choice([1, 2]),
            'task_two_3': random.choice([1, 2]), 'task_two_4': random.choice([1, 2]),
            'task_two_5': random.choice([1, 2]), 'task_two_6': random.choice([1, 2]),
            'task_two_7': random.choice([1, 2]), 'task_two_8': random.choice([1, 2]),
            'task_two_9': random.choice([1, 2]), 'task_two_10': random.choice([1, 2]),
        }
        yield(TaskTwoPage, correct_form_field_values)
