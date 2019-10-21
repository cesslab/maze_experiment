from typing import List
from ._builtin import Page, WaitPage

from experiment.lottery import Lottery
from .models import Player

from experiment.lottery import TimedLotteryPairCollection, LotteryTimedPair, PreferredLotteryPairCollection, LotteryPreferencePair


class Payoffs(Page):
    def vars_for_template(self):
        timed_lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        timed_pair: LotteryTimedPair = timed_lottery_collection.selected_lottery_pair()

        left_timed_lottery: Lottery = timed_pair.left_lottery
        right_timed_lottery: Lottery = timed_pair.right_lottery

        preferred_lottery_collection: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
        preferred_pair: LotteryPreferencePair = preferred_lottery_collection.selected_lottery_pair()
        return {
            'l': left_timed_lottery,
            'r': right_timed_lottery,
            'p': preferred_pair.realized_lottery,
            'ppair': preferred_pair,
            'preferred_pair_number': preferred_lottery_collection.selected_pair_number(),
            'timed_pair_number': timed_lottery_collection.selected_pair_number(),
            'lp': timed_pair
        }


page_sequence = [
    Payoffs
]
