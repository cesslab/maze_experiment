from ._builtin import Page

from experiment.mazes import Maze

from experiment.lottery import Lottery, LotteryTimedPair, TimedLotteryPairCollection


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        lottery_pair: LotteryTimedPair = lottery_collection.selected_lottery_pair()

        return {
            'maze_ids': lottery_pair.maze_names(),
            'lottery_pair_number': lottery_collection.selected_pair_number(),
            'lp': lottery_pair,
            'l': lottery_pair.left_lottery,
            'r': lottery_pair.right_lottery,
        }


class LeftMazePrompt(Page):
    def is_displayed(self):
        lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        lottery_pair: LotteryTimedPair = lottery_collection.selected_lottery_pair()

        return lottery_pair.left_time_seconds > 0 and self.round_number == 1


class RightMazePrompt(Page):
    def is_displayed(self):
        lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        lottery_pair: LotteryTimedPair = lottery_collection.selected_lottery_pair()

        return lottery_pair.right_time_seconds > 0 and self.round_number == 2


class LeftMazePage(Page):
    form_model = 'player'
    form_fields = ['solved', 'solve_time_seconds', 'maze_id']

    def is_displayed(self):
        if self.round_number == 1:
            lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
            lottery_pair: LotteryTimedPair = lottery_collection.selected_lottery_pair()

            if lottery_pair.left_time_seconds == 0:
                self.player.solved = False
                self.player.solve_time_seconds = 0
                self.player.maze_id = lottery_pair.left_lottery.maze.name
                return False
            else:
                return True
        else:
            return False

    def vars_for_template(self):
        lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        lottery_pair: LotteryTimedPair = lottery_collection.selected_lottery_pair()

        lottery: Lottery = lottery_pair.left_lottery
        maze: Maze = lottery.maze

        return {
            'seconds_to_solve': lottery_pair.left_time_seconds,
            'maze_img': 'play_maze_fixed_time/img/'+maze.name+'.png',
            'maze_id': maze.name,
            'start_x': maze.start_x,
            'start_y': maze.start_y,
            'end_x': maze.end_x,
            'end_y': maze.end_y,
            'round': lottery_collection.selected_pair_number(),
        }

    def before_next_page(self):
        lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        lottery_pair: LotteryTimedPair = lottery_collection.selected_lottery_pair()

        lottery: Lottery = lottery_pair.left_lottery
        maze: Maze = lottery.maze
        self.player.lottery_id = lottery.id_number

        maze.solved = self.player.solved
        maze.solve_time = self.player.solve_time_seconds

        lottery.determine_payoff()
        self.player.payoff = lottery.payoff + self.player.payoff


class RightMazePage(Page):
    form_model = 'player'
    form_fields = ['solved', 'solve_time_seconds', 'maze_id']

    def is_displayed(self):
        if self.round_number == 2:
            lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
            lottery_pair: LotteryTimedPair = lottery_collection.selected_lottery_pair()

            if lottery_pair.right_time_seconds == 0:
                self.player.solved = False
                self.player.solve_time_seconds = 0
                self.player.maze_id = lottery_pair.right_lottery.maze.name
                return False
            else:
                return True
        else:
            return False

    def vars_for_template(self):
        lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        lottery_pair: LotteryTimedPair = lottery_collection.selected_lottery_pair()

        lottery: Lottery = lottery_pair.right_lottery
        maze: Maze = lottery.maze

        return {
            'seconds_to_solve': lottery_pair.right_time_seconds,
            'maze_img': 'play_maze_fixed_time/img/'+maze.name+'.png',
            'maze_id': maze.name,
            'start_x': maze.start_x,
            'start_y': maze.start_y,
            'end_x': maze.end_x,
            'end_y': maze.end_y,
            'round': lottery_collection.selected_pair_number(),
        }

    def before_next_page(self):
        lottery_collection: TimedLotteryPairCollection = self.participant.vars['time_lottery_pair_collection']
        lottery_pair: LotteryTimedPair = lottery_collection.selected_lottery_pair()

        lottery: Lottery = lottery_pair.right_lottery
        maze: Maze = lottery.maze

        maze.solved = self.player.solved
        maze.solve_time = self.player.solve_time_seconds
        self.player.lottery_id = lottery.id_number

        lottery.determine_payoff()
        self.player.payoff = lottery.payoff + self.player.payoff


page_sequence = [Instructions, LeftMazePrompt, LeftMazePage, RightMazePrompt, RightMazePage]

