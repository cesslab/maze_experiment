from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from experiment.lottery import Lottery


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        maze_ids = []
        for lottery_pair in self.participant.vars['preferred_lotteries']:
            for lottery in lottery_pair:
                maze_ids.append(lottery.maze.name)

        return {
            'maze_ids': maze_ids,
        }


class MazePage(Page):
    form_model = 'player'
    form_fields = ['solved', 'solve_time_seconds', 'maze_id']

    def vars_for_template(self):
        lottery_pair = self.participant.vars['preferred_lotteries'][self.round_number - 1]
        left_lottery: Lottery = lottery_pair[0]
        right_lottery: Lottery = lottery_pair[1]

        if left_lottery.is_preference:
            maze = left_lottery.maze
        else:
            maze = right_lottery.maze

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
