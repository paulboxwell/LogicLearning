# logic_learning.py
import random

class LogicLearningAI:
    def __init__(self):
        self.outputs = {"00": "00", "01": "00", "10": "00", "11": "00"}
        self.scores = {"00": 0, "01": 0, "10": 0, "11": 0}
        self.round_inputs = []  # Track the inputs used during the round

    def get_output(self, game_input):
        # Record the input used in this round
        self.round_inputs.append(game_input)
        return self.outputs[game_input]

    def round_complete(self, result):
        # Update scores based on the result of the round
        for game_input in self.round_inputs:
            if result == "won":
                self.scores[game_input] += 1
            else:
                self.scores[game_input] -= 1

        if result == "lost":
            # Identify input with the lowest score and update its output
            lowest_score_input = min(self.scores, key=self.scores.get)  # Find input with lowest score
            self.outputs[lowest_score_input] = format(random.randint(0, 3), '02b')  # Change its output
            self.scores[lowest_score_input] = 0
            print(f"Updated Outputs: {self.outputs}")
        print(f"scores: {self.scores}")
        # Clear round inputs for the next round
        self.round_inputs = []