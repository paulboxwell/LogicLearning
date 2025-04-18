# game.py
class Game:
    def __init__(self):
        self.inputs = ["00", "01", "10", "11"]
        self.correct_outputs = ["11", "00", "10", "01"]  # Example correct outputs

    def play_turn(self, ai_output):
        feedback = []
        for inp, output in zip(self.inputs, ai_output):
            feedback.append("won" if output == self.correct_outputs[self.inputs.index(inp)] else "lost")
        return feedback

    def has_won(self, feedback):
        return all(result == "won" for result in feedback)