# main.py
from game import Game
from logic_learning import LogicLearningAI

def main():
    game = Game()
    ai = LogicLearningAI()
    rounds = 0

    while True:
        game.reset_position()
        rounds = 0
        while True:
            rounds += 1
            game_input = game.get_input()
            ai_output = ai.get_output(game_input)
            game.move(ai_output)

            if game.is_won():
                ai.update_scores(game_input, "won")
                print(f"AI won the round in {rounds} moves!")
                break
            elif game.is_lost(rounds):
                ai.update_scores(game_input, "lost")
                print(f"AI lost the round after {rounds} moves.")
                break

        # Check if the AI has mastered all inputs
        if all(score > 0 for score in ai.scores.values()):
            print("AI has mastered the game!")
            break

if __name__ == "__main__":
    main()