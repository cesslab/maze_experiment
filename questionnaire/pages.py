from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class PartOne(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'major', 'year_in_college']


page_sequence = [PartOne]
