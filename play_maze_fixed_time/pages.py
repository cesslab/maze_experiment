from ._builtin import Page

from experiment.lottery import Lottery, LotteryPreferencePair, PreferredLotteryPairCollection
from experiment.mazes import Maze


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        lottery_collection: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
        lottery_pair: LotteryPreferencePair = lottery_collection.selected_lottery_pair()

        return {
            'maze_ids': lottery_pair.maze_names(),
            'left_lottery': lottery_pair.left_lottery,
            'right_lottery': lottery_pair.right_lottery,
            'realized_lottery': lottery_pair.realized_lottery,
            'preference_number': lottery_pair.lottery_label,
            'realized_preference_number': lottery_pair.realized_lottery_label,
            'lottery_pair_number': lottery_collection.selected_pair_number(),
            'l': lottery_pair.left_lottery,
            'r': lottery_pair.right_lottery,
            'l_rate_length': len(lottery_pair.left_lottery.completion_rate),
            'r_rate_length': len(lottery_pair.right_lottery.completion_rate)
        }


class MazePage(Page):
    form_model = 'player'
    form_fields = ['solved', 'solve_time_seconds', 'maze_id']

    def vars_for_template(self):
        lottery_collection: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
        lottery_pair: LotteryPreferencePair = lottery_collection.selected_lottery_pair()
        maze: Maze = lottery_pair.realized_lottery.maze
        return {
            'label': lottery_pair.realized_lottery_label,
            'lottery_pair_number': lottery_collection.selected_pair_number(),
            'seconds_to_solve': self.session.config['max_maze_solve_time'],
            'maze_img': 'play_maze_fixed_time/img/'+maze.name+'.png',
            'maze_id': maze.name,
            'start_x': maze.start_x,
            'start_y': maze.start_y,
            'end_x': maze.end_x,
            'end_y': maze.end_y,
            'round': self.round_number,
        }

    def before_next_page(self):
        lottery_collection: PreferredLotteryPairCollection = self.participant.vars['preferred_lottery_pair_collection']
        lottery_pair: LotteryPreferencePair = lottery_collection.selected_lottery_pair()
        lottery: Lottery = lottery_pair.realized_lottery
        maze: Maze = lottery.maze

        maze.solved = self.player.solved
        maze.solve_time = self.player.solve_time_seconds

        lottery.determine_payoff()
        self.player.payoff = lottery.payoff
        print("Payoff fixed time maze: {}".format(self.player.payoff))


page_sequence = [Instructions, MazePage]
