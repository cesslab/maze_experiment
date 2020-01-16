import random
from typing import List

from otree.api import Currency, Currency as c


class Option:
    # TODO: Remove redundant alternative probability
    A = 1
    B = 2

    def __init__(self, option_type, prob_high, payoff_high: Currency, prob_low, payoff_low: Currency):
        self.option_type = option_type
        self.prob_low = prob_low
        self.payoff_low = payoff_low
        self.prob_high = prob_high
        self.payoff_high = payoff_high

        self.random_num = random.randint(0, 100)
        if self.random_num <= prob_high:
            self.payoff = self.payoff_high
        else:
            self.payoff = self.payoff_low

    def label(self):
        return 'A' if self.option_type == Option.A else 'B'


class Case:
    def __init__(self, option_a, option_b):
        self.option_a = option_a
        self.option_b = option_b
        self.selected_option = None

    def select_option(self, o):
        if o == Option.A:
            self.selected_option = self.option_a
        else:
            self.selected_option = self.option_b


class TaskSeven:
    def __init__(self):
        self.cases: List[Case] = [
            Case(Option(Option.A, 10, c(2.0), 90, c(1.6)), Option(Option.B, 10, c(3.85), 90, c(.1))),
            Case(Option(Option.A, 20, c(2.0), 80, c(1.6)), Option(Option.B, 20, c(3.85), 80, c(.1))),
            Case(Option(Option.A, 30, c(2.0), 70, c(1.6)), Option(Option.B, 30, c(3.85), 70, c(.1))),
            Case(Option(Option.A, 40, c(2.0), 60, c(1.6)), Option(Option.B, 40, c(3.85), 60, c(.1))),
            Case(Option(Option.A, 50, c(2.0), 50, c(1.6)), Option(Option.B, 50, c(3.85), 50, c(.1))),
            Case(Option(Option.A, 60, c(2.0), 40, c(1.6)), Option(Option.B, 60, c(3.85), 40, c(.1))),
            Case(Option(Option.A, 70, c(2.0), 30, c(1.6)), Option(Option.B, 70, c(3.85), 30, c(.1))),
            Case(Option(Option.A, 80, c(2.0), 20, c(1.6)), Option(Option.B, 80, c(3.85), 20, c(.1))),
            Case(Option(Option.A, 90, c(2.0), 10, c(1.6)), Option(Option.B, 90, c(3.85), 10, c(.1))),
            Case(Option(Option.A, 100, c(2.0), 0, c(1.6)), Option(Option.B, 10, c(3.85), 0, c(.1))),
        ]
        self.payoff_case_number = random.randint(1, len(self.cases))
        self._payoff_option = None

    def payoff_case(self) -> Case:
        return self.cases[self.payoff_case_number - 1]

    @property
    def payoff_option(self) -> Option:
        return self._payoff_option

    @payoff_option.setter
    def payoff_option(self, o):
        if o == Option.A:
            self._payoff_option = self.payoff_case().option_a
        else:
            self._payoff_option = self.payoff_case().option_b


class TaskEight:
    def __init__(self):
        self.cases: List[Case] = [
            Case(Option(Option.A, 100, c(8), 0, c(4)), Option(Option.B, 100, c(8), 0, c(4))),
            Case(Option(Option.A, 90, c(8), 10, c(4)), Option(Option.B, 90, c(8), 10, c(4))),
            Case(Option(Option.A, 80, c(8), 20, c(4)), Option(Option.B, 80, c(8), 20, c(4))),
            Case(Option(Option.A, 70, c(8), 30, c(4)), Option(Option.B, 70, c(8), 30, c(4))),
            Case(Option(Option.A, 60, c(8), 40, c(4)), Option(Option.B, 60, c(8), 40, c(4))),
            Case(Option(Option.A, 50, c(8), 50, c(6)), Option(Option.B, 50, c(8), 50, c(4))),
            Case(Option(Option.A, 40, c(8), 60, c(4)), Option(Option.B, 40, c(8), 60, c(4))),
            Case(Option(Option.A, 30, c(8), 70, c(4)), Option(Option.B, 30, c(8), 70, c(4))),
            Case(Option(Option.A, 20, c(8), 80, c(4)), Option(Option.B, 20, c(8), 80, c(4))),
            Case(Option(Option.A, 10, c(8), 90, c(4)), Option(Option.B, 10, c(8), 90, c(4))),
            Case(Option(Option.A, 0, c(8), 100, c(4)), Option(Option.B, 0, c(8), 100, c(4))),
        ]
        self.payoff_case_number = random.randint(1, len(self.cases))
        self._payoff_option = None

    def payoff_case(self) -> Case:
        return self.cases[self.payoff_case_number - 1]

    @property
    def payoff_option(self) -> Option:
        return self._payoff_option

    @payoff_option.setter
    def payoff_option(self, o):
        if o == Option.A:
            self._payoff_option = self.payoff_case().option_a
        else:
            self._payoff_option = self.payoff_case().option_b


class TaskOne:
    def __init__(self):
        self.cases: List[Case] = [
            Case(Option(Option.A, 100, c(8), 0, c(4)), Option(Option.B, 100, c(8), 0, c(0))),
            Case(Option(Option.A, 90, c(8), 10, c(4)), Option(Option.B, 90, c(8), 10, c(0))),
            Case(Option(Option.A, 80, c(8), 20, c(4)), Option(Option.B, 80, c(8), 20, c(0))),
            Case(Option(Option.A, 70, c(8), 30, c(4)), Option(Option.B, 70, c(8), 30, c(0))),
            Case(Option(Option.A, 60, c(8), 40, c(4)), Option(Option.B, 60, c(8), 40, c(0))),
            Case(Option(Option.A, 50, c(8), 50, c(6)), Option(Option.B, 50, c(8), 50, c(0))),
            Case(Option(Option.A, 40, c(8), 60, c(4)), Option(Option.B, 40, c(8), 60, c(0))),
            Case(Option(Option.A, 30, c(8), 70, c(4)), Option(Option.B, 30, c(8), 70, c(0))),
            Case(Option(Option.A, 20, c(8), 80, c(4)), Option(Option.B, 20, c(8), 80, c(0))),
            Case(Option(Option.A, 10, c(8), 90, c(4)), Option(Option.B, 10, c(8), 90, c(0))),
            Case(Option(Option.A, 0, c(8), 100, c(4)), Option(Option.B, 0, c(8), 100, c(0))),
        ]
        self.payoff_case_number = random.randint(1, len(self.cases))
        self._payoff_option = None

    def payoff_case(self) -> Case:
        return self.cases[self.payoff_case_number - 1]

    @property
    def payoff_option(self) -> Option:
        return self._payoff_option

    @payoff_option.setter
    def payoff_option(self, o):
        if o == Option.A:
            self._payoff_option = self.payoff_case().option_a
        else:
            self._payoff_option = self.payoff_case().option_b
