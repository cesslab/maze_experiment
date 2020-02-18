from ._builtin import Page

from experiment.lottery import Lottery

from experiment.lottery import TimedLotteryPairCollection, LotteryTimedPair, PreferredLotteryPairCollection, LotteryPreferencePair

from experiment.tasks import TaskEpsilon

class Payoffs(Page):
    def vars_for_template(self):
        timed_lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        timed_pair: LotteryTimedPair = timed_lottery_collection.selected_lottery_pair()

        left_timed_lottery: Lottery = timed_pair.left_lottery
        right_timed_lottery: Lottery = timed_pair.right_lottery

        preferred_lottery_collection: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
        preferred_pair: LotteryPreferencePair = preferred_lottery_collection.selected_lottery_pair()

        task_epsilon: TaskEpsilon = self.participant.vars['task_epsilon']

        return {
            'l': left_timed_lottery,
            'r': right_timed_lottery,
            'p': preferred_pair.realized_lottery,
            'plabel': 'V' if preferred_pair.realized_lottery_label == 0 else 'W',
            'ppair': preferred_pair,
            'preferred_pair_number': preferred_lottery_collection.selected_lottery_pair_round_number(),
            'timed_pair_number': timed_lottery_collection.selected_lottery_pair_round_number(),
            'lp': timed_pair,
            'cases': task_epsilon.cases,
            'case': task_epsilon.payoff_case(),
            'task_number': self.participant.vars['payment_task_number'],
            'case_number': task_epsilon.payoff_case_number,
            'option': task_epsilon.payoff_option,
            'option_label': task_epsilon.payoff_option.label(),
            'total_payoff': self.participant.payoff,
            'total_payoff_participation': self.participant.payoff_plus_participation_fee(),
            'participation_fee': self.session.config['participation_fee']
        }


page_sequence = [Payoffs]
