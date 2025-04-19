# game.py
import random

class Game:
    def __init__(self):
        self.target_x = 0
        self.target_y = 0
        self.reset_position()
        self.board_size = 21  # Define grid boundaries
        self.current_x = 0
        self.current_y = 0

    def reset_position(self):
        self.current_x = 0
        self.current_y = 0
        while self.is_won():
            self.current_x = random.randint(-10, 10)
            self.current_y = random.randint(-10, 10)

    def get_input(self):
        input = ""
        if self.current_x < self.target_x:
            input += "0"
        else:
            input += "1"
        if self.current_y < self.target_y:
            input += "0"
        else:
            input += "1"
        return input

    def move(self, direction):
        if direction == "11":  # Move Southeast
            self.current_x -= 1
            self.current_y -= 1
        elif direction == "10":  # Move Southwest
            self.current_x -= 1
            self.current_y += 1
        elif direction == "01":  # Move Northeast
            self.current_x += 1
            self.current_y -= 1
        elif direction == "00":  # Move Northwest
            self.current_x += 1
            self.current_y += 1

    def is_out_of_bounds(self):
        # Check if the current position is outside the grid boundaries
        half_size = self.board_size // 2
        return not (-half_size <= self.current_x <= half_size and -half_size <= self.current_y <= half_size)

    def is_won(self):
        distance = abs(self.current_x) + abs(self.current_y)
        return distance <= 2

    def is_lost(self, moves):
        distance = abs(self.current_x) + abs(self.current_y)
        return moves > 40 or self.is_out_of_bounds()

    def print_board(self):
        # Create a simple visual representation of the board
        board = [["." for _ in range(self.board_size)] for _ in range(self.board_size)]

        # Center the board and plot target and current position
        center = self.board_size // 2
        target_x = center + self.target_x
        target_y = center - self.target_y
        current_x = center + self.current_x
        current_y = center - self.current_y

        # Mark positions on the board
        if 0 <= target_x < self.board_size and 0 <= target_y < self.board_size:
            board[target_y][target_x] = "T"  # Target position
        if 0 <= current_x < self.board_size and 0 <= current_y < self.board_size:
            board[current_y][current_x] = "C"  # Current position

        # Print the board
        print("\nBoard:")
        for row in board:
            print(" ".join(row))