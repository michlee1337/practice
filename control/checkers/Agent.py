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
            board.val = self._utility(board)
            return(None, board.val)
        board.val = -float("inf")
        best_move = None
        for next_board in board.next_boards():
            _, next_v = self._getMin(next_board,a,b,d+1)
            if next_v > board.val:
                board.val = next_v
                best_move = next_board
            if board.val >= b:
                return(best_move, board.val)
            a = max(a,board.val)
        return(best_move, board.val)

    def _getMin(self,board,a,b,d):
        if d == self.max_depth:
            board.val = self._utility(board)
            return(None, board.val)
        board.val = float("inf")
        best_move = None
        for next_board in board.next_boards():
            _, next_v = self._getMax(next_board,a,b,d+1)
            if next_v < board.val:
                board.val = next_v
                best_move = next_board
            if board.val <= a:
                return(best_move, board.val)
            b = min(b,board.val)
        return(best_move, board.val)

    def move(self,board):
        a,v = self._getMax(board,-float("inf"),float("inf"),0)
        return(a)
