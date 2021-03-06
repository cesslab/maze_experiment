from ._builtin import Page
from experiment.lottery import LotteryTimedPair, TimedLotteryPairCollection


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class NextNotification(Page):
    def is_displayed(self):
        return self.round_number != 1

    def vars_for_template(self) -> dict:
        return {
            'round_number': self.round_number
        }


class TimeAllocationPage(Page):
    form_model = 'player'
    form_fields = ['left_lottery_time', 'right_lottery_time']

    def vars_for_template(self):
        lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        lottery_pair: LotteryTimedPair = lottery_collection.round_pair(self.round_number)
        return {
            'l': lottery_pair.left_lottery,
            'r': lottery_pair.right_lottery,
            'max_time_seconds': self.session.config['max_time_seconds'],
        }

    def before_next_page(self):
        lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        lottery_pair: LotteryTimedPair = lottery_collection.round_pair(self.round_number)

        # Save the left and right lottery ID  to the player model
        self.player.left_lottery_id = lottery_pair.left_lottery.id_number
        self.player.right_lottery_id = lottery_pair.right_lottery.id_number

        # Save the time allocated to the lottery pair
        lottery_pair.left_time_seconds = self.player.left_lottery_time
        lottery_pair.right_time_seconds = self.player.right_lottery_time

    def error_message(self, values):
        max_time = self.session.config['max_time_seconds']
        left = values['left_lottery_time']
        right = values['right_lottery_time']
        if left == "" or right == "":
            return "Time allocation, in seconds, is required for both V and W."

        left_val = int(left)
        right_val = int(right)
        if left_val + right_val != max_time:
            return "The time in seconds for V and W must add up to exactly {}".format(max_time)


page_sequence = [Instructions, NextNotification, TimeAllocationPage]
