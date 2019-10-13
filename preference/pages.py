from ._builtin import Page
from experiment.lottery import Lottery, LotteryPreferencePair, PreferredLotteryPairCollection


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class ChoicePage(Page):
    form_model = 'player'
    form_fields = ['preference']

    def vars_for_template(self):
        lottery_collection: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
        lottery_pair: LotteryPreferencePair = lottery_collection.round_pair(self.round_number)
        return {
            'l': lottery_pair.left_lottery,
            'r': lottery_pair.right_lottery,
        }

    def before_next_page(self):
        lottery_collection: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
        lottery_pair: LotteryPreferencePair = lottery_collection.round_pair(self.round_number)

        # Save the left and right lottery ID to the player model
        self.player.left_lottery_id = lottery_pair.left_lottery.id_number
        self.player.right_lottery_id = lottery_pair.right_lottery.id_number

        # Save the player's preferred lottery
        lottery_pair.preferred_lottery_label = self.player.preference


page_sequence = [Instructions, ChoicePage]
