from ._builtin import Page
from experiment.lottery import Lottery, LotteryPreferencePair, LotteryPreferencePairCollection


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class ChoicePage(Page):
    form_model = 'player'
    form_fields = ['preference']

    def vars_for_template(self):
        lottery_collection: LotteryPreferencePairCollection = self.participant.vars['preferred_lottery_collection']
        lottery_pair: LotteryPreferencePair = lottery_collection.round_pair(self.round_number)
        return {
            'l': lottery_pair.left_lottery,
            'r': lottery_pair.right_lottery,
        }

    def before_next_page(self):
        lottery_collection: LotteryPreferencePairCollection = self.participant.vars['preferred_lottery_collection']
        lottery_pair: LotteryPreferencePair = lottery_collection.round_pair(self.round_number)

        left_lottery: Lottery = lottery_pair.left_lottery
        right_lottery: Lottery = lottery_pair.right_lottery

        self.player.left_lottery_id = left_lottery.id_number
        self.player.right_lottery_id = right_lottery.id_number

        lottery_pair.preference = self.player.preference


page_sequence = [Instructions, ChoicePage]
