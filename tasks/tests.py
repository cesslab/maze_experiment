import random

from ._builtin import Bot
from otree.api import SubmissionMustFail

from .pages import TaskOne, TaskTwoPage, TaskThree, TaskFour, TaskFive, TaskSix, TaskSeven, Instructions


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

        # Test task 3
        incorrect_form_field_values = {
            'task_three_1': '', 'task_three_2': '', 'task_three_3': '', 'task_three_4': '', 'task_three_5': '',
            'task_three_6': '', 'task_three_7': '', 'task_three_8': '', 'task_three_9': '', 'task_three_10': '',
            'task_three_bet': ''
        }
        yield(SubmissionMustFail(TaskThree, incorrect_form_field_values))

        correct_form_field_values = {
            'task_three_1': random.choice([1, 2]), 'task_three_2': random.choice([1, 2]),
            'task_three_3': random.choice([1, 2]), 'task_three_4': random.choice([1, 2]),
            'task_three_5': random.choice([1, 2]), 'task_three_6': random.choice([1, 2]),
            'task_three_7': random.choice([1, 2]), 'task_three_8': random.choice([1, 2]),
            'task_three_9': random.choice([1, 2]), 'task_three_10': random.choice([1, 2]),
            'task_three_bet': random.choice([1, 2])
        }
        yield(TaskThree, correct_form_field_values)

        # Test task 4
        incorrect_form_field_values = {
            'task_four_1': '', 'task_four_2': '', 'task_four_3': '', 'task_four_4': '', 'task_four_5': '',
            'task_four_6': '', 'task_four_7': '', 'task_four_8': '', 'task_four_9': '', 'task_four_10': '',
            'task_four_bet': ''
        }
        yield(SubmissionMustFail(TaskFour, incorrect_form_field_values))

        incorrect_form_field_values = {
            'task_four_1': 1, 'task_four_2': 2, 'task_four_3': 1, 'task_four_4': 1, 'task_four_5': 1,
            'task_four_6': 2, 'task_four_7': 1, 'task_four_8': 2, 'task_four_9': 2, 'task_four_10': 2,
            'task_four_bet': ''
        }
        yield(SubmissionMustFail(TaskFour, incorrect_form_field_values))

        correct_form_field_values = {
            'task_four_1': random.choice([1, 2]), 'task_four_2': random.choice([1, 2]),
            'task_four_3': random.choice([1, 2]), 'task_four_4': random.choice([1, 2]),
            'task_four_5': random.choice([1, 2]), 'task_four_6': random.choice([1, 2]),
            'task_four_7': random.choice([1, 2]), 'task_four_8': random.choice([1, 2]),
            'task_four_9': random.choice([1, 2]), 'task_four_10': random.choice([1, 2]),
            'task_four_bet': random.choice([1, 2])
        }
        yield(TaskFour, correct_form_field_values)

        # Test task 5
        incorrect_form_field_values = {
            'task_five_invested': ''
        }
        yield(SubmissionMustFail(TaskFive, incorrect_form_field_values))

        incorrect_form_field_values = {
            'task_five_invested': random.randint(101, 200)
        }
        yield(SubmissionMustFail(TaskFive, incorrect_form_field_values))

        correct_form_field_values = {
            'task_five_invested': random.randint(0, 100)
        }
        yield(TaskFive, correct_form_field_values)

        # Test task 6
        incorrect_form_field_values = {
            'task_six_invested': ''
        }
        yield(SubmissionMustFail(TaskSix, incorrect_form_field_values))

        incorrect_form_field_values = {
            'task_six_invested': random.randint(101, 200)
        }
        yield(SubmissionMustFail(TaskSix, incorrect_form_field_values))

        correct_form_field_values = {
            'task_six_invested': random.randint(0, 100)
        }
        yield(TaskSix, correct_form_field_values)

        # Test task 7
        incorrect_form_field_values = {
            'distance': '',
            'unit': ''
        }
        yield(SubmissionMustFail(TaskSeven, incorrect_form_field_values))
        incorrect_form_field_values = {
            'distance': '1200',
            'unit': ''
        }
        yield(SubmissionMustFail(TaskSeven, incorrect_form_field_values))

        correct_form_field_values = {
            'distance': '1200',
            'unit': '1'
        }
        yield(TaskSeven, correct_form_field_values)
