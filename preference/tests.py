from otree.api import expect
from ._builtin import Bot

from preference.pages import Instructions, ChoicePage, NextNotification
from experiment.lottery import LotteryPreferencePair, PreferredLotteryPairCollection, Lottery


class PlayerBot(Bot):

    def play_round(self):

        if self.round_number == 1:
            yield(Instructions)
            # Choose left lottery
            yield(ChoicePage, dict(preference=LotteryPreferencePair.LEFT))
            expect(self.player.preference, LotteryPreferencePair.LEFT)

            # Get the lottery pair for the round
            lottery_collection: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
            lottery_pair: LotteryPreferencePair = lottery_collection.round_pair(self.round_number)

            self.test_preferred_lottery_label_returned(LotteryPreferencePair.LEFT, lottery_pair)
            self.test_realized_lottery_matches_preference(lottery_pair, lottery_pair.left_lottery)

        elif self.round_number == 2:
            yield(NextNotification)

            # Choose right lottery
            yield(ChoicePage, dict(preference=LotteryPreferencePair.RIGHT))

            # Get the lottery pair for the round
            lottery_collection: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
            lottery_pair: LotteryPreferencePair = lottery_collection.round_pair(self.round_number)

            self.test_preferred_lottery_label_returned(LotteryPreferencePair.RIGHT, lottery_pair)
            self.test_realized_lottery_matches_preference(lottery_pair, lottery_pair.right_lottery)

        else:
            yield(NextNotification)

            yield(ChoicePage, dict(preference=LotteryPreferencePair.EITHER))

            lottery_collection: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
            lottery_pair: LotteryPreferencePair = lottery_collection.round_pair(self.round_number)

            self.test_preferred_lottery_label_returned(LotteryPreferencePair.EITHER, lottery_pair)
            self.test_realized_lottery_label_when_either_lottery_is_preferred(lottery_pair)
            self.test_correct_realized_lottery_number_returned_when_either_is_preference(lottery_pair)

        lottery_collection: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
        lottery_pair: LotteryPreferencePair = lottery_collection.round_pair(self.round_number)

        self.test_lottery_maze_names(lottery_pair)

    @staticmethod
    def test_preferred_lottery_label_returned(lottery_label, lottery_pair: LotteryPreferencePair):
        expect(lottery_pair.lottery_label, lottery_label)

    @staticmethod
    def test_realized_lottery_matches_preference(lottery_pair: LotteryPreferencePair, preferred_lottery: Lottery):
        expect(lottery_pair.realized_lottery.id_number, preferred_lottery.id_number)

    @staticmethod
    def test_realized_lottery_label_when_either_lottery_is_preferred(lottery_pair: LotteryPreferencePair):
        assert(lottery_pair.realized_lottery_label in [LotteryPreferencePair.LEFT, LotteryPreferencePair.RIGHT])

    @staticmethod
    def test_correct_realized_lottery_number_returned_when_either_is_preference(lottery_pair: LotteryPreferencePair):
        assert(lottery_pair.realized_lottery.id_number in [lottery_pair.left_lottery.id_number, lottery_pair.right_lottery.id_number])

    @staticmethod
    def test_lottery_maze_names(lottery_pairs: LotteryPreferencePair):
        assert(len(lottery_pairs.maze_names()) == 2)
