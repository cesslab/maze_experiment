from otree.api import Currency as c, currency_range, expect
from . import pages
from ._builtin import Bot
from .models import Constants

from preference.pages import Instructions, ChoicePage
from experiment.lottery import LotteryPreferencePair, LotteryPreferencePairCollection


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield(Instructions)
            yield(ChoicePage, dict(preference=LotteryPreferencePair.LEFT))
            # Test left lottery preferred
            expect(self.player.preference, LotteryPreferencePair.LEFT)
            lottery_collection: LotteryPreferencePairCollection = self.participant.vars['preferred_lottery_collection']
            lottery_pair: LotteryPreferencePair = lottery_collection.round_pair(self.round_number)
            expect(lottery_pair.preference, "Left")
            expect(lottery_pair.realized_lottery.id_number, lottery_pair.left_lottery.id_number)
        elif self.round_number == 2:
            yield(ChoicePage, dict(preference=LotteryPreferencePair.RIGHT))
            # Test right  lottery preferred
            expect(self.player.preference, LotteryPreferencePair.RIGHT)
            lottery_collection: LotteryPreferencePairCollection = self.participant.vars['preferred_lottery_collection']
            lottery_pair: LotteryPreferencePair = lottery_collection.round_pair(self.round_number)
            expect(lottery_pair.preference, "Right")
            expect(lottery_pair.realized_lottery.id_number, lottery_pair.right_lottery.id_number)
        else:
            yield(ChoicePage, dict(preference=LotteryPreferencePair.EITHER))
            # Test either lottery preferred
            expect(self.player.preference, LotteryPreferencePair.EITHER)
            lottery_collection: LotteryPreferencePairCollection = self.participant.vars['preferred_lottery_collection']
            lottery_pair: LotteryPreferencePair = lottery_collection.round_pair(self.round_number)
            expect(lottery_pair.preference, "Either")

