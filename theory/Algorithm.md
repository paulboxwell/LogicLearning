## Mathematical Description of the Logic Learning Algorithm

Consider a decision function:
\[
F: \{00,\,01,\,10,\,11\} \to \{00,\,01,\,10,\,11\},
\]
which maps an observation to an action. Alongside this mapping, maintain a score function:
\[
S: \{00,\,01,\,10,\,11\} \to \mathbb{Z},
\]
with all scores initially set to 0. We can describe the learning process as follows:

1. **Initialization:**  
   For each \( o \in \{00,\,01,\,10,\,11\} \), if \( F(o) \) is undefined or uninitialized (denoted by "xx"), then set:
   \[
   F(o) \ \text{= a random element of} \ \{00,\,01,\,10,\,11\}.
   \]

2. **Round Dynamics:**  
   During a *round*, the game runs with the current mapping \( F \). Let \( \mathcal{O}_r \subseteq \{00, 01, 10, 11\} \) be the set of all unique observations encountered during that round. In each move:

   - The current state \( s \) produces an observation \( o = f(s) \).
   - The AI outputs an action \( a = F(o) \).
   - The state updates as \( s \gets s + d \) where the displacement \( d \) is determined by \( a \).

3. **Feedback and Learning Update:**

   At the end of a round, a binary outcome \( R \) is provided:
   
   - **If the round is won (\( R = \text{won} \)):**  
     Update the scores for every encountered observation:
     \[
     S(o) \leftarrow S(o) + 1 \quad \forall\, o \in \mathcal{O}_r.
     \]

   - **If the round is lost (\( R = \text{lost} \)):**  
     First, penalize every observation seen during the round:
     \[
     S(o) \leftarrow S(o) - 1 \quad \forall\, o \in \mathcal{O}_r.
     \]
     Then, identify the observation \( o^* \) with the lowest score:
     \[
     o^* = \operatorname*{argmin}_{o\in \mathcal{O}_r} S(o).
     \]
     Finally, adjust the action for \( o^* \) by incrementing its value cyclically (interpreting the action as an integer in \( \{0,1,2,3\} \)):
     \[
     F(o^*) \leftarrow \text{binary}\bigl((\text{int}(F(o^*)) + 1) \bmod 4\bigr),
     \]
     and reset its score:
     \[
     S(o^*) \leftarrow 0.
     \]

4. **Convergence Criterion:**  
   The learning process is halted when all scores exceed a given threshold (for example, when
   \[
   S(o) > 10 \quad \text{for all } o \in \{00,\,01,\,10,\,11\}
   \]
   indicating that the mapping \( F \) is stable and the AI consistently wins).
