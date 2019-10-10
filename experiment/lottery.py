import random
from typing import List
from otree.api import Currency
from experiment.mazes import Maze


class Lottery:
    def __init__(self, id_number: int, high_prize: Currency, low_prize: Currency, completion_rate: List[int],
                 prob_completed: int, prob_incomplete: int, maze: Maze):
        self.id_number: int = id_number
        self.low_prize: Currency = low_prize
        self.high_prize: Currency = high_prize
        self.completion_rate: List[int] = completion_rate
        self.prob_completed: int = prob_completed
        self.prob_incomplete: int = prob_incomplete
        self.is_preference = False
        self.time_limit = None
        self.maze: Maze = maze


class LotteryPreferencePair:
    LEFT = 1
    EITHER = 2
    RIGHT = 3

    def __init__(self, a: Lottery, b: Lottery):
        pair = [a, b]
        random.shuffle(pair)
        self.left_lottery = pair[0]
        self.right_lottery = pair[1]
        self.preference = None


class LotteryTimedPair:
    def __init__(self, a: Lottery, b: Lottery):
        pair = [a, b]
        random.shuffle(pair)
        self.left_lottery = pair[0]
        self.right_lottery = pair[1]
        self.left_time_seconds = None
        self.right_time_seconds = None
