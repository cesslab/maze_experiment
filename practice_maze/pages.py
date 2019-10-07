from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from experiment.mazes import Maze


class Instructions(Page):
    pass


class PracticeMaze(Page):
    form_model = 'player'
    form_fields = ['solved', 'solve_time_seconds', 'maze_id']

    def vars_for_template(self):
        maze = Maze('closed', 147, 2, 169, 314)


        return {
            'seconds_to_solve': 120,
            'maze_img': 'practice_maze/img/'+maze.name+'.png',
            'maze_id': maze.name,
            'start_x': maze.start_x,
            'start_y': maze.start_y,
            'end_x': maze.end_x,
            'end_y': maze.end_y,
        }


page_sequence = [Instructions, PracticeMaze]
