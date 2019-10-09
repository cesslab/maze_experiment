import random

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from experiment.lottery import Lottery
from experiment.mazes import Maze


class Constants(BaseConstants):
    name_in_url = 'preference'
    players_per_group = None
    num_rounds = 4


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                # TODO: Create a LotteryPair class that will store the players preferred lottery, if any
                lotteries = [
                    [
                        Lottery(1, c(8), c(4), [50], 50, 50, Maze('40_40_1', 147, 2, 169, 314)),
                        Lottery(2, c(8), c(4), [50], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
                    ],
                    [
                        Lottery(3, c(8), c(4), [50], 80, 20, Maze('40_40_1', 147, 2, 169, 314)),
                        Lottery(4, c(8), c(4), [50], 80, 20, Maze('60_40_1', 147, 2, 169, 314))
                    ],
                    [
                        Lottery(5, c(8), c(4), [40, 60], 80, 20, Maze('40_40_1', 147, 2, 169, 314)),
                        Lottery(6, c(10), c(2), [50], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
                    ],
                    [
                        Lottery(7, c(10.44), c(2), [30], 60, 40, Maze('40_40_1', 147, 2, 169, 314)),
                        Lottery(8, c(8), c(4), [80], 60, 40, Maze('60_40_1', 147, 2, 169, 314))
                    ],
                ]
                random.shuffle(lotteries)
                for pair in lotteries:
                    random.shuffle(pair)
                player.participant.vars['preferred_lotteries'] = lotteries
                # randomly choose one of the pairs for payment
                random_preferred_lottery_pair_id = random.randint(0, Constants.num_rounds-1)
                player.participant.vars['preferred_pair_id'] = random_preferred_lottery_pair_id
                player.participant.vars['timed_pair_id'] = random.randint(0, Constants.num_rounds-1)
                player.participant.vars["preferred_lottery_pair"] = lotteries[random_preferred_lottery_pair_id]
                player.participant.vars["preferred_lottery"] = None



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    left_lottery_id = models.IntegerField(default=False)
    right_lottery_id = models.IntegerField(default=False)
    preference = models.IntegerField(default=False)
    chosen_lottery = models.IntegerField(default=False)
