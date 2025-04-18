# game.py
import random

class Game:
    def __init__(self):
        self.target_x = 0
        self.target_y = 0
        self.reset_position()

    def reset_position(self):
        self.current_x = random.randint(-10, 10)
        self.current_y = random.randint(-10, 10)

    def get_input(self):
        if self.current_x < 0 and self.current_y > 0:
            return "11"  # Northwest
        elif self.current_x > 0 and self.current_y < 0:
            return "00"  # Southeast
        elif self.current_x > 0 and self.current_y > 0:
            return "10"  # Northeast
        else:
            return "01"  # Southwest

    def move(self, direction):
        if direction == "00":  # Move Southeast
            self.current_x += 1
            self.current_y -= 1
        elif direction == "01":  # Move Southwest
            self.current_x -= 1
            self.current_y -= 1
        elif direction == "10":  # Move Northeast
            self.current_x += 1
            self.current_y += 1
        elif direction == "11":  # Move Northwest
            self.current_x -= 1
            self.current_y += 1

    def is_won(self):
        distance = abs(self.current_x) + abs(self.current_y)
        return distance <= 2

    def is_lost(self, rounds):
        distance = abs(self.current_x) + abs(self.current_y)
        return distance > 12 or rounds > 12