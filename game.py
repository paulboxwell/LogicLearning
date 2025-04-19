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
        if direction == "11":  # Move Southeast
            self.current_x += 1
            self.current_y -= 1
        elif direction == "10":  # Move Southwest
            self.current_x -= 1
            self.current_y -= 1
        elif direction == "01":  # Move Northeast
            self.current_x += 1
            self.current_y += 1
        elif direction == "00":  # Move Northwest
            self.current_x -= 1
            self.current_y += 1

    def is_won(self):
        distance = abs(self.current_x) + abs(self.current_y)
        return distance <= 2

    def is_lost(self, rounds):
        distance = abs(self.current_x) + abs(self.current_y)
        return distance > 22 or rounds > 12

    def print_board(self):
        # Create a simple visual representation of the board
        board_size = 21
        board = [["." for _ in range(board_size)] for _ in range(board_size)]

        # Center the board and plot target and current position
        center = board_size // 2
        target_x = center + self.target_x
        target_y = center - self.target_y
        current_x = center + self.current_x
        current_y = center - self.current_y

        # Mark positions on the board
        if 0 <= target_x < board_size and 0 <= target_y < board_size:
            board[target_y][target_x] = "T"  # Target position
        if 0 <= current_x < board_size and 0 <= current_y < board_size:
            board[current_y][current_x] = "C"  # Current position

        # Print the board
        print("\nBoard:")
        for row in board:
            print(" ".join(row))