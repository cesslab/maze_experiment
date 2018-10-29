class Lottery:
    def __init__(self, id_number, high_prize, low_prize, completion_rate, prob_completed, prob_incomplete):
        self.id_number = id_number
        self.low_prize = low_prize
        self.high_prize = high_prize
        self.completion_rate = completion_rate
        self.prob_completed = prob_completed
        self.prob_incomplete = prob_incomplete
