---

# LogicLearning

LogicLearning is a small-scale project that experimentally explores a logic learning AI designed to master a simple navigation game. The project uses a basic reinforcement-style algorithm to adjust a mapping from discrete observations to diagonal move actions until the AI consistently reaches a target in as few rounds as possible.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [The Game](#the-game)
- [The Algorithm](#the-algorithm)
- [Distribution of Results](#distribution-of-results)
- [Further Reading and References](#further-reading-and-references)
- [License](#license)

---

## Overview

LogicLearning creates an environment where an AI is tasked with navigating a bounded two-dimensional grid. The game is defined by a starting state, a target zone, and moves that are strictly diagonal. The AI’s challenge is to learn the correct response for each possible observation (derived from the sign of its coordinates) to consistently reach the target using as few rounds as possible.

This project was inspired and informed by the ideas presented in the article “[Logic Learning AI](https://exploreai.blogspot.com/2013/04/logic-learning-ai.html)” on ExploreAI, which examines how simple learning algorithms can evolve strategies over iterative trials.

---

## Project Structure

- **`game.py`**  
  Defines the `Game` class which is responsible for:
  - Setting up the game board (a grid with boundaries).
  - Randomly initializing game positions.
  - Translating the current state into a binary observation based on the signs of the coordinates.
  - Enforcing game constraints such as win (reaching near the target) and loss (exceeding move bounds or going out of bounds).
  - Optionally printing the board for visualization.

- **`logic_learning.py`**  
  Contains the `LogicLearningAI` class that:
  - Maintains a mapping \( F: \{00, 01, 10, 11\} \to \{00, 01, 10, 11\} \) (from input to output moves).
  - Records scores for each mapping based on round outcomes.
  - Adjusts the move corresponding to the observation with the poorest performance when a round is lost.
  - Uses a simple, incremental (hill-climbing) learning strategy to evolve a successful mapping.

- **`main.py`**  
  Acts as the driver script:
  - Integrates the game and the logic learning algorithm.
  - Runs multiple simulations (or “rounds”) to determine how many iterations are needed for the AI to reliably win.
  - Displays a summary of results, such as the number of rounds required for mastery and the average performance over several runs.

---

## The Game

Mathematically, the game can be represented as follows:

- **State Representation:**  
  The game state is a point on a 2D integer grid:
  \[
  s = (x, y) \quad \text{with} \quad x, y \in \mathbb{Z} \quad \text{and} \quad |x|, |y| \leq 10.
  \]
  The target state is fixed at the origin \( s_{\text{target}} = (0, 0) \), with the win condition defined by the Manhattan distance:
  \[
  |x| + |y| \leq 2.
  \]

- **Observations:**  
  The game computes a binary observation for each coordinate:
  \[
  o = \big(I(x),\, I(y)\big) \quad \text{where} \quad I(z) = \begin{cases} 0, & z < 0 \\ 1, & z \ge 0 \end{cases}
  \]
  This gives the four possible inputs: `00`, `01`, `10`, and `11`.

- **Actions:**  
  The available actions are 2-bit strings corresponding to diagonal moves:
  
  | Action | Move Vector      |
  |--------|------------------|
  | `00`   | \( (+1, +1) \)   |
  | `01`   | \( (+1, -1) \)   |
  | `10`   | \( (-1, +1) \)   |
  | `11`   | \( (-1, -1) \)   |

- **Transition & Terminal Conditions:**  
  The state updates via:
  \[
  s' = s + d \quad \text{(with } d \text{ from the chosen action)}
  \]
  A move is considered a win if the state reaches near the origin and a loss if it exceeds a set move count (e.g., 40 moves) or leaves the predefined grid boundaries.

---

## The Algorithm

The logic learning algorithm is a simple reinforcement method aimed at converging on an optimal mapping from observations to actions.

1. **Initialization:**  
   The decision function \( F \) is defined from input observations to one of the four possible diagonal moves. Initially, each mapping is undefined (represented as `"xx"`) or initialized to a random move.

2. **Learning Process:**  
   During a round, as the game state changes, the AI:
   - Observes the state and produces an output \( a = F(o) \) for each observation \( o \).
   - Records all observations encountered during that round.
   
3. **Feedback and Update:**
   - **Winning Round:**  
     If the AI wins the round, it reinforces the current mapping by incrementing scores \( S(o) \) for every observation \( o \) seen in that round.
   - **Losing Round:**  
     If the round is lost, the algorithm penalizes by decrementing scores, and then identifies the observation with the lowest score. The corresponding output is adjusted:
     \[
     F(o^*) \leftarrow \text{binary}\bigl((\text{int}(F(o^*)) + 1) \mod 4\bigr)
     \]
     and its score is reset.
     
4. **Convergence:**  
   The process continues over multiple rounds until a threshold (e.g., all scores exceeding 10) is reached—indicating that the AI’s mapping is robust and consistently wins the game.

This algorithm essentially performs a **tabular hill-climbing** search in the discrete space of 256 possible mappings (with four inputs each mapping to one of four outputs).

---

## Distribution of Results

The learning process is executed over several runs (for example, 1000 runs by default). Each run tracks:

- **Rounds per Run:**  
  The number of rounds required for the AI to achieve mastery (i.e., when the winning strategy has been established).

- **Statistical Summaries:**  
  At the end of the simulation, the project outputs:
  - A list of rounds taken for each run.
  - The average number of rounds required across all runs.

These results help compare the efficiency of the current algorithm against potential alternatives. In future explorations, one might compare this simple reinforcement policy with other methods such as tabular Q-learning, policy gradient methods, or evolutionary algorithms.

---

## Further Reading and References

This project and its approach are inspired by concepts discussed in the article [Logic Learning AI](https://exploreai.blogspot.com/2013/04/logic-learning-ai.html) available on Explore AI. The article provides thoughtful insights into how minimalistic algorithms can learn control strategies by iteratively refining their decision-making rules.

For further exploration, consider:
- **Tabular Q-Learning:** An approach that updates Q-values based on reward and estimated future value.
- **Policy Gradient Methods:** Optimizing a probability distribution over actions.
- **Evolutionary Algorithms:** Directly searching through the space of mappings using mutation and selection criteria.

Each method has its own trade-offs in terms of convergence rate and sample efficiency.

---

## License

_This project is provided for educational purposes. Feel free to explore, modify, and extend the work._

---
