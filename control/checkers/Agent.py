class Agent:
    '''
    A depth limited minimax search agent with alpha beta pruning
    reference: AI modern approach
    '''

    def __init__(self, max_depth, heuristic):
        self.max_depth = max_depth
        # self.heuristic = heuristic
        # EXT: choose heuristics
        ## safe checkers
        ## kings

    def _utility(self, board):
        balance = 0
        for row in board.state:
            for cell in row:
                if cell == 0:
                    pass
                elif cell.belongsToAgent:
                    balance += 1
                else:
                    balance -= 1
        return balance

    def _getMax(self,board,a,b,d):
        if d == self.max_depth:
            return(None, self._utility(board))
        v = -float("inf")
        best_move = None
        for next_board in board.next_boards():
            _, next_v = self._getMin(next_board,a,b,d+1)
            if next_v > v:
                v = next_v
                best_move = next_board
            if v >= b:
                return(best_move, v)
            a = max(a,v)
        return(best_move, v)

    def _getMin(self,board,a,b,d):
        if d == self.max_depth:
            return(None, self._utility(board))
        v = float("inf")
        best_move = None
        for next_board in board.next_boards():
            _, next_v = self._getMax(next_board,a,b,d+1)
            if next_v < v:
                v = next_v
                best_move = next_board

                return(best_move, v)
            b = min(b,v)
        return(best_move, v)

    def move(self,board):
        a,v = self._getMax(board,-float("inf"),float("inf"),0)
        return(a)
