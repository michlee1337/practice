from Agent import *
from Board import *

class Move:
    def __init__(self, start_position, end_position, board):
        self.difficulty = difficulty
        # smtg about heuristics
class Game:
    depth_lookup = {
        1: 3,
        2: 5,
        3: 10
    } # might be tweaked

    def __init__(self, heuristic = 0):
        self.board = Board()
        self.difficulty = self._getDifficulty()
        self.agent = Agent(Game.depth_lookup[self.difficulty], heuristic)
        self.isAgentTurn = False # start on human turn

    def _getDifficulty(self):
        diff = 0
        while True:
            diff = eval(input("What level of difficulty? (1 Easy, 2 Medium, 3 Hard) "))
            if diff == 1 or diff == 2 or diff == 3:
                break
            print("Please enter an integer between 1 and 3")
        return diff

    def _getAgentMove(self):
        return self.agent.move(self.board)

    def _getHumanMove(self):
        possibles = self.board.next_boards()

        for i,b in enumerate(possibles):
            print("Move {}:".format(i))
            print(b)
            print('\n')

        while True:
            m = eval(input("Choose a move by inputting the move number: "))
            if m >= 0 and m < len(possibles):
                break
            print("Please choose a valid move!")
        return(possibles[m])

    def checkWin(self, forAgent):
        return self.board.noPieces(not forAgent)

    def play(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        if self.isAgentTurn: # agent turn
            print("My Turn!")
            self.board = self._getAgentMove()
        else:
            print("Your Turn!")
            self.board = self._getHumanMove()
        print("Board is now: {}".format(self.board))

        if self.checkWin(self.isAgentTurn):
            print("Game Over")
            if self.isAgentTurn:
                print("You lost... Try again?")
            else:
                print("You won!! Try a harder game?")
            return 0
        else:
            self.isAgentTurn = not self.isAgentTurn # change turns
            return self.play()
