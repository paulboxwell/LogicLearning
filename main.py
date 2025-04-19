# main.py
from game import Game
from logic_learning import LogicLearningAI

def run_game(show_board=False):
    game = Game()
    ai = LogicLearningAI()
    rounds = 0

    while True:  # Learning session
        game.reset_position()
        moves = 0

        while True:  # Round loop
            moves += 1
            game_input = game.get_input()
            ai_output = ai.get_output(game_input)
            game.move(ai_output)

            # Optionally display the board
            if show_board:
                print("input: ", game_input, " Output: ", ai_output)
                input("")
                game.print_board()

            if game.is_won():
                print(f"Round {rounds} Won in {moves} moves!")
                ai.round_complete("won")
                break
            elif game.is_lost(moves):
                print(f"Round {rounds} Lost in {moves} moves!")
                ai.round_complete("lost")
                rounds += 1
                break

        # Check if the AI has mastered all inputs
        if all(score > 10 for score in ai.scores.values()):
            print(f"AI has mastered the game after {rounds} rounds!")
            print(ai.outputs)
            return rounds  # Return the number of rounds it took to master the game

def main(show_board=False, num_runs=10):
    results = []

    for run in range(num_runs):
        print(f"Starting Run {run + 1}")
        rounds_to_learn = run_game(show_board)
        results.append(rounds_to_learn)

    print("\nSummary of Results:")
    print(f"Rounds to learn for each run: {results}")
    print(f"Average rounds to learn: {sum(results) / len(results):.2f}")

if __name__ == "__main__":
    # Enable or disable board printing by passing True or False to `main`
    # Specify the number of runs with `num_runs`
    main(show_board=False, num_runs=1000)