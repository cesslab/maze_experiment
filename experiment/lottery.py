class Lottery:
    def __init__(self, id_number, high_prize, low_prize, completion_rate, prob_high_completed, prob_low_incomplete):
        self.id_number = id_number
        self.low_prize = low_prize
        self.high_prize = high_prize
        self.completion_rate = completion_rate
        self.prob_high_completed = prob_high_completed
        self.prob_low_incomplete = prob_low_incomplete
