# Checkers Minimax Agent
This is a Checkers simulation against a Checkers AI agent playable via the command line.

The Checkers agent uses a minimax algorithm.

The simulation is set up according to American Checkers rules.
The agent was created with reference to Russell, S., & Norvig, P. (2002). Artificial intelligence: a modern approach.

# To Play
Run `python checkers.py`

You will receive command line prompts for what search depth and heuristic level you'd like the agent to use.


You will also receive prompts to choose your move by inputting the index of the move you'd like to perform from displayed possible moves.


Good luck!

# To Test
Run `python test.py`

It will run 20 simulations for each possible configuration (excluding difficulty hard in interest of runtime) and output a dictionary of wins deduct losses.

# Code structure
`checkers.py` contains the very short driver code.

All the other files are Class definitions. More details on each class is included in a comment included before their init functions.
- the driver code imports from Game.
- Game imports from Agent and Board.
- Board imports from Piece.
- Agent is completely independent.
