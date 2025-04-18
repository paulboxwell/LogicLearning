# main.py
from game import Game
from logic_learning import LogicLearningAI

def main():
    game = Game()
    ai = LogicLearningAI()
    rounds = 0

    while True:
        rounds += 1
        game.reset_position()
        moves = 0

        while True:
            moves += 1
            game_input = game.get_input()
            ai_output = ai.get_output(game_input)
            game.move(ai_output)

            if game.is_won():
                print(f"AI won the round in {moves} moves!")
                ai.round_complete("won")
                break
            elif game.is_lost(moves):
                print(f"AI lost the round after {moves} moves.")
                ai.round_complete("lost")
                break

        # Check if the AI has mastered all inputs
        if all(score > 10 for score in ai.scores.values()):
            print(f"AI has mastered the game after {rounds}")
            print(ai.outputs)
            break

if __name__ == "__main__":
    main()