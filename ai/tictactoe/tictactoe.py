"""
Tic Tac Toe Player
"""
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count,o_count=0,0

    for row in board:
        for i in row:
            if i == X:
                x_count+=1
            elif i == O:
                o_count+=1
            elif i != EMPTY:
                return f'Invaild input: {i}'
    
    return "X's turn" if o_count == x_count else "O's turn"
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves= set()
    for row in range(len(board)):
        for i in range(len(board[row])):
            if board[row][i] == EMPTY:
                possible_moves.add((row,i))

    return possible_moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError('Invaild action/move')
    else:
        board[action[0]][action[1]]=player(board)[0]
    
    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #horizontally
    for row in board:
        if O not in row:
            return X
        elif X not in row:
            return O
    #Vertically
    for col in range(len(board)):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            return board[0][col]
    #diagonally
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] or board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[1][1]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for row in board:
        if EMPTY in row:
            return False
    return True
        
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

def minimax(board= initial_state()):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(state):
        if utility(state) != None:
            return "Tie" if winner(state) == None else f"Player {winner(state)} wins"

        counter = math.inf()
        for action in actions(state):
            counter = max(counter,min_value(result(state,action)))
        return counter
    
    def min_value(state):
        if utility(state) != None:
            return "Tie" if winner(state) == None else f"Player {winner(state)} wins"

        counter = math.inf()
        for action in actions(state):
            counter = min(counter,max_value(result(state,action)))
        return counter

    max_value(board)

minimax()