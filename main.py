# main.py
from game import Game
from logic_learning import LogicLearningAI

def main():
    game = Game()
    ai = LogicLearningAI()

    attempts = 0
    while True:
        attempts += 1
        ai_output = ai.get_output()
        feedback = game.play_turn(ai_output)

        if game.has_won(feedback):
            print(f"AI succeeded after {attempts} attempts!")
            break
        else:
            ai.update_output(feedback)

if __name__ == "__main__":
    main()