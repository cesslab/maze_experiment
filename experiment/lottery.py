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
        self.maze: Maze = maze


class LotteryPreferencePair:
    LEFT = 0
    RIGHT = 1
    EITHER = 2

    def __init__(self, a: Lottery, b: Lottery):
        self.pair = [a, b]
        random.shuffle(self.pair)
        self._preferred_lottery_label = None
        self.realized_lottery = None
        self.realized_lottery_label = None

    def maze_names(self):
        return [self.left_lottery.maze.name, self.right_lottery.maze.name]

    @property
    def left_lottery(self):
        return self.pair[self.LEFT]

    @property
    def right_lottery(self):
        return self.pair[self.RIGHT]

    @property
    def preferred_lottery_label(self):
        return self._preferred_lottery_label

    @preferred_lottery_label.setter
    def preferred_lottery_label(self, label: int):
        """
        Sets both the preference number and the realized lottery
        :param label:
        :return:
        """
        self._preferred_lottery_label = label
        if label == self.LEFT:
            self.realized_lottery = self.left_lottery
        elif label == self.RIGHT:
            self.realized_lottery = self.right_lottery
        # Either
        else:
            self.realized_lottery_label = random.choice([self.LEFT, self.RIGHT])
            self.realized_lottery = self.pair[self.realized_lottery_label]


class LotteryTimedPair:
    def __init__(self, a: Lottery, b: Lottery):
        pair = [a, b]
        random.shuffle(pair)
        self.left_lottery = pair[0]
        self.right_lottery = pair[1]
        self.left_time_seconds = None
        self.right_time_seconds = None


class PreferredLotteryPairCollection:
    def __init__(self):
        self.collection = [
                    LotteryPreferencePair(
                        Lottery(1, Currency(8), Currency(4), [50], 50, 50, Maze('40_40_1', 147, 2, 169, 314)),
                        Lottery(2, Currency(8), Currency(4), [50], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
                    ),
                    LotteryPreferencePair(
                        Lottery(3, Currency(8), Currency(4), [50], 80, 20, Maze('40_40_1', 147, 2, 169, 314)),
                        Lottery(4, Currency(8), Currency(4), [50], 80, 20, Maze('60_40_1', 147, 2, 169, 314))
                    ),
                    LotteryPreferencePair(
                        Lottery(5, Currency(8), Currency(4), [40, 60], 80, 20, Maze('40_60_2', 147, 2, 169, 314)),
                        Lottery(6, Currency(10), Currency(2), [50], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
                    ),
                    LotteryPreferencePair(
                        Lottery(7, Currency(10.44), Currency(2), [30], 60, 40, Maze('40_60_2', 147, 2, 169, 314)),
                        Lottery(8, Currency(8), Currency(4), [80], 60, 40, Maze('60_40_2', 147, 2, 169, 314))
                    ),
            ]
        random.shuffle(self.collection)
        self.selected_pair_index = random.randrange(len(self.collection))

    def round_pair(self, round_number):
        return self.collection[round_number-1]

    def selected_lottery_pair(self):
        return self.collection[self.selected_pair_index]

    def selected_pair_number(self):
        return self.selected_pair_index + 1

    def is_round_pair_selected(self, round_number):
        return round_number == self.selected_pair_number()


class TimedLotteryPairCollection:
    def __init__(self):
        self.collection = [
                LotteryPreferencePair(
                    Lottery(1, Currency(8), Currency(4), [50], 50, 50, Maze('40_40_1', 147, 2, 169, 314)),
                    Lottery(2, Currency(8), Currency(4), [50], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
                ),
                LotteryPreferencePair(
                    Lottery(3, Currency(8), Currency(4), [50], 80, 20, Maze('40_40_1', 147, 2, 169, 314)),
                    Lottery(4, Currency(8), Currency(4), [50], 80, 20, Maze('60_40_1', 147, 2, 169, 314))
                ),
                LotteryPreferencePair(
                    Lottery(5, Currency(8), Currency(4), [40, 60], 80, 20, Maze('40_60_2', 147, 2, 169, 314)),
                    Lottery(6, Currency(10), Currency(2), [50], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
                ),
                LotteryPreferencePair(
                    Lottery(7, Currency(10.44), Currency(2), [30], 60, 40, Maze('40_60_2', 147, 2, 169, 314)),
                    Lottery(8, Currency(8), Currency(4), [80], 60, 40, Maze('60_40_2', 147, 2, 169, 314))
                ),
        ]

        random.shuffle(self.collection)
        self.selected_pair_index = random.randrange(len(self.collection))

    def round_pair(self, round_number):
        return self.collection[round_number-1]

    def selected_lottery_pair(self):
        return self.collection[self.selected_pair_index]

    def selected_pair_number(self):
        return self.selected_pair_index + 1

    def is_round_pair_selected(self, round_number):
        return round_number == self.selected_pair_number()
