# logic_learning.py
import random

class LogicLearningAI:
    def __init__(self):
        self.outputs = {"00": "xx", "01": "xx", "10": "xx", "11": "xx"}  # Start all outputs as "xx"
        self.scores = {"00": 0, "01": 0, "10": 0, "11": 0}
        self.round_inputs = set()  # Track unique inputs used during the round

    def get_output(self, game_input):
        # If the AI hasn't seen this input before, make a random guess
        if self.outputs[game_input] == "xx":
            self.outputs[game_input] = format(random.randint(0, 3), '02b')  # Random 2-bit output

        # Record the input used in this round
        self.round_inputs.add(game_input)
        return self.outputs[game_input]

    def round_complete(self, result):
        # Update scores based on the result of the round
        if result == "won":
            for game_input in self.round_inputs:
                self.scores[game_input] += 1
        elif result == "lost":
            for game_input in self.round_inputs:
                self.scores[game_input] -= 1

            # Identify input with the lowest score
            lowest_score_input = min(self.scores, key=self.scores.get)

            # Ensure the new guess differs from the current value
            current_value = self.outputs[lowest_score_input]
            new_value = current_value
            while new_value == current_value:
                new_value = format(random.randint(0, 3), '02b')  # Generate new random output
            
            self.outputs[lowest_score_input] = new_value
            self.scores[lowest_score_input] = 0  # Reset score for new guess
        print(f"Outputs:\t{self.outputs}")

        print(f"Scores: \t{self.scores}")
        # Clear round inputs for the next round
        self.round_inputs = set()