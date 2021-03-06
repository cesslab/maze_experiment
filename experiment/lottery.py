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
        self.is_completion_rate_range = True if len(self.completion_rate) > 1 else False

        self.random_value = random.randint(1, 100)
        self.payoff = None

    def determine_payoff(self):
        if self.maze.solved:
            if self.random_value <= self.prob_completed:
                self.payoff = self.high_prize
            else:
                self.payoff = self.low_prize
        else:
            if self.random_value <= self.prob_incomplete:
                self.payoff = self.high_prize
            else:
                self.payoff = self.low_prize

    def __str__(self):
        return "low: {}, high: {}, maze comp: {}, high|complete: {} high|incomplete: {}".format(
            self.low_prize, self.high_prize, self.completion_rate_str(), self.prob_completed, self.prob_incomplete
        )

    def completion_rate_str(self):
        if self.is_completion_rate_range:
            return "{}, {}".format(self.completion_rate[0], self.completion_rate[1])
        else:
            return "{}".format(self.completion_rate[0])


class LotteryPair:
    LEFT = 0
    RIGHT = 1
    EITHER = 2

    def __init__(self, a: Lottery, b: Lottery):
        self.pair = [a, b]
        random.shuffle(self.pair)

    def maze_names(self) -> List[str]:
        return [self.left_lottery.maze.name, self.right_lottery.maze.name]

    @property
    def left_lottery(self) -> Lottery:
        return self.pair[self.LEFT]

    @property
    def right_lottery(self) -> Lottery:
        return self.pair[self.RIGHT]

    def __str__(self):
        return "left: {}, right: {}".format(self.left_lottery, self.right_lottery)


class LotteryPreferencePair(LotteryPair):
    def __init__(self, a: Lottery, b: Lottery):
        super(LotteryPreferencePair, self).__init__(a, b)
        self._lottery_label = None
        # The player's preferred lottery, or the randomly selected lottery if the player's preference is either, chosen
        # from this pair of lotteries.
        self.realized_lottery = None
        # The label for the preferred lottery selected by the player.
        # Possible values are: is Left = 0, Right = 1, or Either = 2
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
    def lottery_label(self):
        return self._lottery_label

    @lottery_label.setter
    def lottery_label(self, label: int):
        """
        This function sets the realized lottery, which is the player's preferred lottery chosen from this lottery pair,
        or if the player preferred either of the lotteries one is chosen at random.
        :param label:
        :return:
        """
        self._lottery_label = label
        if label == self.LEFT:
            self.realized_lottery = self.left_lottery
            self.realized_lottery_label = self.LEFT
        elif label == self.RIGHT:
            self.realized_lottery = self.right_lottery
            self.realized_lottery_label = self.RIGHT
        # Either
        else:
            self.realized_lottery_label = random.choice([self.LEFT, self.RIGHT])
            self.realized_lottery = self.pair[self.realized_lottery_label]


class LotteryTimedPair(LotteryPair):
    def __init__(self, a: Lottery, b: Lottery):
        super(LotteryTimedPair, self).__init__(a, b)
        self.left_time_seconds = None
        self.right_time_seconds = None


class LotteryCollection:
    """
    0, L1 Z, Y, omega, eta, rho
    ---------------------------
    1, L1 800, 400, 50, 60, 40
    2, L2 800, 400, 50, 80, 20
    3, L3 800, 400, [0,100], 60, 40
    4, L4 1000, 200, 50, 60, 40
    5, L2' 800, 400, 50, 100, 0
    6, L2'' 800, 400, 50, 30, 0
    7, L3' 800, 400, [40, 60], 60, 40
    8, L4' 1200, 0, 50, 60, 40
    """
    def __init__(self, selected_pair_index):
        self.collection = [
            # 0: L1 vs L2
            LotteryPreferencePair(
                Lottery(1, Currency(8), Currency(4), [50], 60, 40, Maze('40_40_1', 147, 2, 169, 314)),
                Lottery(2, Currency(8), Currency(4), [50], 80, 20, Maze('60_40_1', 147, 2, 169, 314))
            ),
            # 1: L1 vs L2'
            LotteryPreferencePair(
                Lottery(3, Currency(8), Currency(4), [50], 60, 40, Maze('40_40_1', 147, 2, 169, 314)),
                Lottery(4, Currency(8), Currency(4), [50], 10, 0, Maze('60_40_1', 147, 2, 169, 314))
            ),
            # 2: L1 vs L2''
            LotteryPreferencePair(
                Lottery(5, Currency(8), Currency(4), [50], 60, 40, Maze('40_40_1', 147, 2, 169, 314)),
                Lottery(6, Currency(8), Currency(4), [50], 30, 0, Maze('60_40_1', 147, 2, 169, 314))
            ),
            # 3: L1 vs L3
            LotteryPreferencePair(
                Lottery(7, Currency(8), Currency(4), [50], 60, 40, Maze('60_40_1', 147, 2, 169, 314)),
                Lottery(8, Currency(8), Currency(4), [0, 100], 60, 40, Maze('50_50_2', 147, 2, 169, 314))
            ),
            # 4: L1 vs L3'
            LotteryPreferencePair(
                Lottery(9, Currency(8), Currency(4), [50], 60, 40, Maze('40_40_1', 147, 2, 169, 314)),
                Lottery(10, Currency(8), Currency(4), [40, 60], 60, 40, Maze('40_60_2', 147, 2, 169, 314))
            ),
            # 5: L1 vs L4
            LotteryPreferencePair(
                Lottery(11, Currency(8), Currency(4), [50], 60, 40, Maze('40_40_1', 147, 2, 169, 314)),
                Lottery(12, Currency(10), Currency(2), [50], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
            ),
            # 6: L1 vs L4'
            LotteryPreferencePair(
                Lottery(13, Currency(8), Currency(4), [50], 60, 40, Maze('40_40_1', 147, 2, 169, 314)),
                Lottery(14, Currency(12), Currency(0), [50], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
            ),
            # 7: Added by Mauricio
            LotteryPreferencePair(
                Lottery(15, Currency(8), Currency(4), [50], 60, 40, Maze('40_40_1', 147, 2, 169, 314)),
                Lottery(16, Currency(8), Currency(4), [50], 100, 0, Maze('60_40_1', 147, 2, 169, 314))
            ),
        ]
        self.selected_pair_index = selected_pair_index
        self._order = list(range(0, len(self.collection)))
        random.shuffle(self._order)

    def round_pair(self, round_number):
        return self.collection[self._order[round_number - 1]]

    def selected_lottery_pair(self):
        return self.collection[self._order[self.selected_pair_index]]

    def selected_lottery_pair_round_number(self):
        return self._order[self.selected_pair_index] + 1

    def is_round_pair_selected(self, round_number):
        return self._order[round_number - 1] == self.selected_pair_index


class PreferredLotteryPairCollection(LotteryCollection):
    def __init__(self):
        super(PreferredLotteryPairCollection, self).__init__(3)


class TimedLotteryPairCollection(LotteryCollection):
    def __init__(self):
        super(TimedLotteryPairCollection, self).__init__(4)

