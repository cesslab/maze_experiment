from otree.api import expect, Submission
from ._builtin import Bot

from .pages import Instructions, ChoicePage, NextNotification
from experiment.lottery import LotteryPreferencePair, PreferredLotteryPairCollection, Lottery


class PlayerBot(Bot):

    cases = [LotteryPreferencePair.LEFT, LotteryPreferencePair.RIGHT, LotteryPreferencePair.EITHER]

    def play_round(self):
        print(f"Playing round {self.round_number}, case: {self.case}")
        if self.round_number == 1:
            yield Instructions
        else:
            yield NextNotification

        yield ChoicePage, dict(preference=self.case)
        expect(self.player.preference, self.case)

        lotteries: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
        lottery_pair: LotteryPreferencePair = lotteries.round_pair(self.round_number)

        expect(lottery_pair.lottery_label, self.case)
        if self.case == LotteryPreferencePair.LEFT:
            expect(lottery_pair.realized_lottery.id_number, lottery_pair.left_lottery.id_number)
        elif self.case == LotteryPreferencePair.RIGHT:
            expect(lottery_pair.realized_lottery.id_number, lottery_pair.right_lottery.id_number)
        else:
            expect(lottery_pair.realized_lottery_label in [LotteryPreferencePair.LEFT, LotteryPreferencePair.RIGHT], True)
            expect(lottery_pair.realized_lottery.id_number in [lottery_pair.left_lottery.id_number, lottery_pair.right_lottery.id_number], True)
