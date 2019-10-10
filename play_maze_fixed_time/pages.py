from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from experiment.lottery import Lottery, LotteryPreferencePair, LotteryPreferencePairCollection
from experiment.mazes import Maze


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        lottery_collection: LotteryPreferencePairCollection = self.participant.vars['preferred_lottery_collection']
        lottery_pair: LotteryPreferencePair = lottery_collection.round_pair(self.round_number)

        return {
            'maze_ids': lottery_pair.maze_names(),
            'left_lottery': lottery_pair.left_lottery,
            'right_lottery': lottery_pair.right_lottery,
            'realized_lottery': lottery_pair.realized_lottery,
            'preference': lottery_pair.preference,
        }


class MazePage(Page):
    form_model = 'player'
    form_fields = ['solved', 'solve_time_seconds', 'maze_id']

    def vars_for_template(self):
        lottery_collection: LotteryPreferencePairCollection = self.participant.vars['preferred_lottery_collection']
        lottery_pair: LotteryPreferencePair = lottery_collection.round_pair(self.round_number)
        maze: Maze = lottery_pair.realized_lottery.maze
        return {
            'seconds_to_solve': self.session.config['max_maze_solve_time'],
            'maze_img': 'play_maze_fixed_time/img/'+maze.name+'.png',
            'maze_id': maze.name,
            'start_x': maze.start_x,
            'start_y': maze.start_y,
            'end_x': maze.end_x,
            'end_y': maze.end_y,
            'round': self.round_number,
        }


page_sequence = [Instructions, MazePage]
