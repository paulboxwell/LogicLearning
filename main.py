# main.py
from game import Game
from logic_learning import LogicLearningAI

def main(show_board=False):
    game = Game()
    ai = LogicLearningAI()
    rounds = 0

    while True: # Learning session
        game.reset_position()
        moves = 0

        while True: # Round Loop
            moves += 1
            game_input = game.get_input()
            ai_output = ai.get_output(game_input)
            game.move(ai_output)

            # Optionally display the board
            if show_board:
                game.print_board()
            input("")
            if game.is_won():
                print(f"AI won the round in {moves} moves!")
                print(game.current_x, " ", game.current_y)
                ai.round_complete("won")
                break
            elif game.is_lost(moves):
                print(f"AI lost the round after {moves} moves.")
                print(game.current_x, " ", game.current_y)
                ai.round_complete("lost")
                rounds += 1
                break
        
        # Check if the AI has mastered all inputs
        if all(score > 10 for score in ai.scores.values()):
            print(f"AI has mastered the game after {rounds}")
            print(ai.outputs)
            break

if __name__ == "__main__":
    # Enable or disable board printing by passing True or False to `main`
    main(show_board=True)