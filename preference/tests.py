from otree.api import expect
from ._builtin import Bot

from preference.pages import Instructions, ChoicePage, NextNotification
from experiment.lottery import LotteryPreferencePair, PreferredLotteryPairCollection, Lottery


class PlayerBot(Bot):

    def test_round_where_lottery_chosen(self, lottery_choice, round_number):
        yield Instructions
        yield ChoicePage, dict(preference=lottery_choice)
        expect(self.player.preference, lottery_choice)

        lotteries: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
        lottery_pair: LotteryPreferencePair = lotteries.round_pair(round_number)

        self.test_player_preference_is_set(lottery_choice, lottery_pair)
        if lottery_choice == LotteryPreferencePair.EITHER:
            self.test_random_lottery_chosen(lottery_pair.realized_lottery_label)
            self.test_correct_realized_lottery_number_returned_when_either_is_preference(lottery_pair)
        else:
            self.test_player_preferred_lottery_matches_selected(lottery_pair, lottery_pair.left_lottery)

    def play_round(self):
        if self.round_number == 1:
            self.test_round_where_lottery_chosen(LotteryPreferencePair.LEFT, self.round_number)
        elif self.round_number == 2:
            self.test_round_where_lottery_chosen(LotteryPreferencePair.RIGHT, self.round_number)
        else:
            self.test_round_where_lottery_chosen(LotteryPreferencePair.EITHER, self.round_number)

    @staticmethod
    def test_player_preference_is_set(preference, lottery_pair: LotteryPreferencePair):
        expect(lottery_pair.lottery_label, preference)

    @staticmethod
    def test_player_preferred_lottery_matches_selected(lottery_pair: LotteryPreferencePair, preferred_lottery: Lottery):
        expect(lottery_pair.realized_lottery.id_number, preferred_lottery.id_number)

    @staticmethod
    def test_random_lottery_chosen(randomly_chosen_lottery_label):
        assert(randomly_chosen_lottery_label in [LotteryPreferencePair.LEFT, LotteryPreferencePair.RIGHT])

    @staticmethod
    def test_correct_realized_lottery_number_returned_when_either_is_preference(lottery_pair: LotteryPreferencePair):
        assert(lottery_pair.realized_lottery.id_number in [lottery_pair.left_lottery.id_number, lottery_pair.right_lottery.id_number])

