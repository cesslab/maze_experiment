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

    def before_next_page(self):
        timed_lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        timed_pair: LotteryTimedPair = timed_lottery_collection.selected_lottery_pair()

        left_timed_lottery: Lottery = timed_pair.left_lottery
        right_timed_lottery: Lottery = timed_pair.right_lottery

        preferred_lottery_collection: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
        preferred_pair: LotteryPreferencePair = preferred_lottery_collection.selected_lottery_pair()

        task_epsilon: TaskEpsilon = self.participant.vars['task_epsilon']
        self.player.part_1_selected_lottery_pair_round_number = preferred_lottery_collection.selected_lottery_pair_round_number()
        self.player.part_1_selected_lottery_id = preferred_pair.lottery_label
        self.player.part_1_selected_lottery_maze_solved = preferred_pair.realized_lottery.maze.solved
        self.player.part_1_random_value = preferred_pair.realized_lottery.random_value
        self.player.part_2_selected_lottery_pair_round_number = timed_lottery_collection.selected_lottery_pair_round_number()
        self.player.part_2_left_maze_solved = left_timed_lottery.maze.solved
        self.player.part_2_left_random_value = left_timed_lottery.random_value
        self.player.part_2_right_maze_solved = right_timed_lottery.maze.solved
        self.player.part_2_right_random_value = right_timed_lottery.random_value
        self.player.part_3_payoff_task_number = self.participant.vars['payment_task_number']
        self.player.part_3_task_epsilon_payoff_case = task_epsilon.payoff_case_number
        self.player.part_3_task_epsilon_option_selected = task_epsilon.payoff_option.option_type
        self.player.part_3_task_epsilon_option_random_number = task_epsilon.payoff_option.random_num






page_sequence = [Payoffs]
