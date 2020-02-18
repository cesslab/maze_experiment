from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from experiment.lottery import Lottery, Maze
from otree.api import (
    Currency
)


class PartOne(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'major', 'year_in_college']


class PartTwo(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']

    def vars_for_template(self) -> dict:
        return {
            'l': Lottery(1, Currency(9), Currency(4), [50], 70, 40, Maze('40_40_1', 147, 2, 169, 314))
        }

page_sequence = [PartOne, PartTwo]
