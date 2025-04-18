# logic_learning.py
import random

class LogicLearningAI:
    def __init__(self):
        self.outputs = {"00": "00", "01": "00", "10": "00", "11": "00"}
        self.scores = {"00": 0, "01": 0, "10": 0, "11": 0}

    def get_output(self, game_input):
        return self.outputs[game_input]

    def update_scores(self, game_input, result):
        if result == "won":
            self.scores[game_input] += 1
        else:
            self.scores[game_input] -= 1
            self.outputs[game_input] = format(random.randint(0, 3), '02b')  # Try a new output