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

    def _getMax(board,a,b):
        if d == self.max_depth:
            return(self._utility(board))
        board.val = -float("inf")
        for next_board in board.next_boards():
            board.val = max(board.val,self._getMin(next_board,a,b))
            if board.val >= b:
                return(board.val)
            a = max(a,board.val)
        return(board.val)

    def _getMin(board,a,b,d):
        if d == self.max_depth:
            return(self._utility(board))
        board.val = float("inf")
        for next_board in board.next_boards():
            board.val = min(board.val,self._getMax(next_board,a,b))
            if board.val <= a:
                return(board.val)
            b = min(b,board.val)
        return(board.val)

    def move(self,board):
        v = self._getMax(board,-float("inf"),float("inf"),0)
        for b in board.next_boards():
            if b.val == v:
                return(b)
        raise RuntimeError("Move with given utility does not exist. Something went wrong during minimax search or move function.")
