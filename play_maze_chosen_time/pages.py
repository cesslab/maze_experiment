from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from experiment.lottery import Lottery
from experiment.mazes import Maze


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        maze_ids = []
        for lottery_pair in self.participant.vars['timed_lotteries']:
            for lottery in lottery_pair:
                maze_ids.append(lottery.maze.name)

        return {
            'maze_ids': maze_ids,
        }


class LeftMazePage(Page):
    form_model = 'player'
    form_fields = ['solved', 'solve_time_seconds', 'maze_id']

    def is_displayed(self):
        lottery_pair = self.participant.vars['timed_lotteries'][self.round_number - 1]
        lottery: Lottery = lottery_pair[0]
        if lottery.time_limit == 0:
            self.player.solved = False
            self.player.solve_time_seconds = 0
            self.player.maze_id = lottery.maze.name
            return False
        else:
            return True

    def vars_for_template(self):
        lottery_pair = self.participant.vars['timed_lotteries'][self.round_number - 1]
        lottery: Lottery = lottery_pair[0]
        maze: Maze = lottery.maze

        return {
            'seconds_to_solve': lottery.time_limit,
            'maze_img': 'play_maze_fixed_time/img/'+maze.name+'.png',
            'maze_id': maze.name,
            'start_x': maze.start_x,
            'start_y': maze.start_y,
            'end_x': maze.end_x,
            'end_y': maze.end_y,
            'round': self.round_number,
        }

    def before_next_page(self):
        pass


class RightMazePage(Page):
    form_model = 'player'
    form_fields = ['solved', 'solve_time_seconds', 'maze_id']

    def is_displayed(self):
        lottery_pair = self.participant.vars['timed_lotteries'][self.round_number - 1]
        lottery: Lottery = lottery_pair[1]
        if lottery.time_limit == 0:
            self.player.solved = False
            self.player.solve_time_seconds = 0
            self.player.maze_id = lottery.maze.name
            return False
        else:
            return True

    def vars_for_template(self):
        lottery_pair = self.participant.vars['timed_lotteries'][self.round_number - 1]
        lottery: Lottery = lottery_pair[1]
        maze: Maze = lottery.maze

        return {
            'seconds_to_solve': lottery.time_limit,
            'maze_img': 'play_maze_fixed_time/img/'+maze.name+'.png',
            'maze_id': maze.name,
            'start_x': maze.start_x,
            'start_y': maze.start_y,
            'end_x': maze.end_x,
            'end_y': maze.end_y,
            'round': self.round_number,
        }


page_sequence = [Instructions, LeftMazePage, RightMazePage]

