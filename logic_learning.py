# logic_learning.py
import random

class LogicLearningAI:
    def __init__(self):
        self.outputs = ["00", "00", "00", "00"]  # Start with a random guess
        self.fail_count = 0

    def update_output(self, feedback):
        for i, result in enumerate(feedback):
            if result == "lost":
                # Modify the output for this input
                self.outputs[i] = format(random.randint(0, 3), '02b')  # Random 2-bit output

    def get_output(self):
        return self.outputs