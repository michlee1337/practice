from Agent import *
from Board import *
from random import randint

class Game:
    '''
    A checkers game with a Command Line Interface.

    Attributes
        - board
        - difficulty
        - agent
        - isAgentTurn: True if it is currently the Agent's turn
        - DEBUG: set to True to make Agent play against RNG.
    Methods
        - checkWin: Check if someone won on the last move.
        - play: Play a move in the game.
    '''
    depth_lookup = {
        1: 3,
        2: 5,
        3: 8
    }

    def __init__(self, difficulty=None,heuristic=None, DEBUG=False):
        if difficulty is None:
            difficulty = self._getDifficulty()
        if heuristic is None:
            heuristic = self._getHeuristic()
        self.board = Board()
        self.difficulty = difficulty
        self.agent = Agent(Game.depth_lookup[self.difficulty], heuristic)
        self.isAgentTurn = False # start on human turn
        self.winner = 0
        self.DEBUG = DEBUG

    def checkDraw(self):
        '''
        Check if current player can't move.
        Output: <Boolean>
        '''
        possibles = self.board.next_boards()
        return len(possibles) == 0

    def checkWin(self):
        '''
        Check if someone won on the last move.
        Output: <Boolean>
        '''
        return self.board.noPieces(not self.isAgentTurn)

    def play(self):
        '''
        Play one move of the game
        '''
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if self.isAgentTurn: # agent turn
            print("My Turn!")
            self.board = self._getAgentMove()
        elif self.DEBUG:
            print("nani")
            self.board = self._getRandMove()
        else:
            print("Your Turn!")
            self.board = self._getHumanMove()
        print("Board is now: {}".format(self.board))

        if self.checkWin():
            print("Game Over")
            if self.isAgentTurn:
                self.winner = 1
                print("You lost... Try again?")
            else:
                self.winner = -1
                print("You won!! Try a harder game?")
            return 0
        elif self.checkDraw():
            print("It's a draw! Tiebreaker?")
            self.winner = 0
        else:
            self.isAgentTurn = not self.isAgentTurn # change turns
            return self.play()

    def _getHeuristic(self):
        while True:
            h = eval(input("What heuristic? (0: simple count, 1: weight kings, 2: weight kings & edges) "))
            if h == 1 or h == 2 or h == 3:
                break
            print("Please enter an integer between 0 and 2")
        return h

    def _getDifficulty(self):
        diff = 0
        while True:
            diff = eval(input("What level of difficulty? (1 Easy, 2 Medium, 3 Hard) "))
            if diff == 1 or diff == 2 or diff == 3:
                break
            print("Please enter an integer between 1 and 3")
        return diff

    def _getRandMove(self):
        possibles = self.board.next_boards()
        return possibles[randint(0,len(possibles)-1)]

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
