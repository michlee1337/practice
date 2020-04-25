class Agent:
    '''
    A depth limited minimax search agent with alpha beta pruning.
    reference: AI modern approach

    Attributes:
        - max_depth: the max depth of the minimax search
        - heuristic: the heuristic used for evaluating states

    Methods
        - move
    '''

    def __init__(self, max_depth, heuristic=0):
        self.max_depth = max_depth
        self.heuristic = heuristic

    def move(self,board):
        '''
        Executes a move informed by minimax search

        Input: Board
        Output: Board

        '''
        a,v = self._getMax(board,-float("inf"),float("inf"),0)
        return(a)

    # internal helper: evaluates curent state using set heuristic
    def _utility(self, board):
        def simpleBalance():
            if piece == 0:
                return(0)
            elif piece.belongsToAgent:
                return(1)
            else:
                return(-1)

        def weightedKings():
            if piece == 0:
                return(0)
            elif piece.belongsToAgent:
                return(1+7*piece.isKing)
            else:
                return(-1-7*piece.isKing)

        def kingsAndEdges():
            edges = [0,7]
            if piece == 0:
                return(0)
            elif piece.belongsToAgent:
                return(1 + 7*piece.isKing + sum([1 for i in [r,c] if i in edges]))
            else:
                return(-1-7*piece.isKing - sum([1 for i in [r,c] if i in edges]))

        heuristics = {
        0: simpleBalance,
        1: weightedKings,
        2: kingsAndEdges
        }

        utility = 0
        for r, row in enumerate(board.state):
            for c, piece in enumerate(row):
                utility += heuristics[self.heuristic]()
        return utility


    # internal helper: gets max next state
    def _getMax(self,board,a,b,d):
        if d == self.max_depth:
            return(board, self._utility(board))
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

    # internal helper: gets min next state
    def _getMin(self,board,a,b,d):
        if d == self.max_depth:
            return(board, self._utility(board))
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
