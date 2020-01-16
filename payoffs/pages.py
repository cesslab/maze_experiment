from ._builtin import Page

from experiment.lottery import Lottery

from experiment.lottery import TimedLotteryPairCollection, LotteryTimedPair, PreferredLotteryPairCollection, LotteryPreferencePair


class Payoffs(Page):
    def vars_for_template(self):
        timed_lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        timed_pair: LotteryTimedPair = timed_lottery_collection.selected_lottery_pair()

        left_timed_lottery: Lottery = timed_pair.left_lottery
        right_timed_lottery: Lottery = timed_pair.right_lottery

        preferred_lottery_collection: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
        preferred_pair: LotteryPreferencePair = preferred_lottery_collection.selected_lottery_pair()

        task_two: TaskTwo = self.participant.vars['task_two']

        return {
            'l': left_timed_lottery,
            'r': right_timed_lottery,
            'p': preferred_pair.realized_lottery,
            'plabel': 'V' if preferred_pair.realized_lottery_label == 0 else 'W',
            'ppair': preferred_pair,
            'preferred_pair_number': preferred_lottery_collection.selected_pair_number(),
            'timed_pair_number': timed_lottery_collection.selected_pair_number(),
            'lp': timed_pair,
            'cases': task_two.cases,
            'case': task_two.payoff_case(),
            'case_number': task_two.payoff_case_number,
            'option': task_two.payoff_option,
            'option_label': task_two.payoff_option.label(),
            'total_payoff': self.participant.payoff,
            'total_payoff_participation': self.participant.payoff_plus_participation_fee(),
            'participation_fee': self.session.config['participation_fee']
        }


page_sequence = [Payoffs]
