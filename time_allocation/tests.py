from otree.api import expect, SubmissionMustFail
from ._builtin import Bot
import random

from time_allocation.pages import Instructions, NextNotification, TimeAllocationPage
from experiment.lottery import LotteryTimedPair, TimedLotteryPairCollection


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield(Instructions)
        else:
            yield(NextNotification)

        # Test incorrect time allocations
        wrong_left_time = random.randint(121, 5000)
        wrong_right_time = -1*random.randint(0, 120)
        SubmissionMustFail(TimeAllocationPage, dict(left_lottery_time=wrong_left_time, right_lottery_time=wrong_right_time))

        # Test correct time allocations
        left_time = random.randint(0, 120)
        yield (TimeAllocationPage, dict(left_lottery_time=left_time, right_lottery_time=120-left_time))

        lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        lottery_pair: LotteryTimedPair = lottery_collection.round_pair(self.round_number)

        expect(lottery_pair.left_time_seconds, left_time)
        expect(lottery_pair.right_time_seconds, 120 - left_time)


