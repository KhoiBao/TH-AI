import math
import copy
import random
import numpy

# Declare object X and O, user and opponent (AI)
X = "X"
O = "0"
EMPTY = None 
user = None
ai = None
board_size = 3
# assume that flag = X and O is player 


# Initialize the starting state of the board
def initial_state():
    return [[EMPTY for _ in range(board_size)] for _ in range(board_size)] # let user decide what is the size of map

# Create player role
def player(board):
    count = 0
    for i in board:
        for j in i:
            if j:
                count += 1
    if count % 2 != 0: # shadowing the state that user is always the first players
        return ai 
    return user 

# represent actions has been made
def actions(board):
    result = set() 
    board_length = len(board)
    for i in range(board_length):
        for j in range(board_length):
            if board[i][j] == EMPTY: 
                result.add((i, j))
    return result

def result(board, action): 
    current_player = player(board)
    result_board = copy.deepcopy(board)
    (i, j) = action
    result_board[i][j] = current_player
    return result_board

# check phuong ngang
def check_horizontal_winner(board): 
    winner_val = None 
    board_length = len(board)
    for i in range(board_length):
        winner_val = board[i][0]
        for j in range(board_length):
            if board[i][j] != winner_val:
                winner_val = None
                break
        if winner_val:
            return winner_val
    return None

# check phuong doc
def check_vertical_winner(board): 
    winner_val = None 
    board_length = len(board)
    for i in range(board_length):
        winner_val = board[0][i]
        for j in range(board_length):
            if board[j][i] != winner_val:
                winner_val = None
                break
        if winner_val:
            return winner_val
    return None

# Check phuong cheo
def check_diagonal_winner(board): 
    winner_val = None 
    board_length = len(board)
    
    # left-to-right diagonal
    winner_val = board[0][0]
    for i in range(board_length):
        if board[i][i] != winner_val:
            winner_val = None
            break
    if winner_val:
        return winner_val

    # right-to-left diagonal
    winner_val = board[0][board_length - 1]
    for i in range(board_length):
        j = board_length - 1 - i
        if board[i][j] != winner_val:
            winner_val = None
            break
    if winner_val:
        return winner_val

    return None

def winner(board):
    winner_val = check_horizontal_winner(board) or check_vertical_winner(board) or check_diagonal_winner(board) or None 
    return winner_val

def terminal(board):
    if winner(board) != None:
        return True
    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True

def utility(board):
    winner_val = winner(board)
    if winner_val == X:
        return 1
    elif winner_val == O:
        return -1
    return 0

# MAX function, represent for AI with Alpha-Beta
def maxValue(state, alpha, beta):
    if terminal(state):
        return utility(state)
    
    v = -math.inf
    for action in actions(state):
        v = max(v, minValue(result(state, action), alpha, beta))
        if v >= beta:  # prune
            return v
        alpha = max(alpha, v)
    return v

# MIN function, represent for Player with Alpha-Beta
def minValue(state, alpha, beta):
    if terminal(state):
        return utility(state)
    
    v = math.inf
    for action in actions(state):
        v = min(v, maxValue(result(state, action), alpha, beta))
        if v <= alpha:  # prune
            return v
        beta = min(beta, v)
    return v

#Returns the optimal action for the current player on the board.
def minimax(board):
    current_player = player(board)
    move = None

    if current_player == X:
        min_val = -math.inf
        for action in actions(board):
            check = minValue(result(board, action), -math.inf, math.inf)
            if check > min_val:
                min_val = check
                move = action
    else:
        max_val = math.inf
        for action in actions(board):
            check = maxValue(result(board, action), -math.inf, math.inf)
            if check < max_val:
                max_val = check
                move = action
    return move


if __name__ == "__main__":
    print("Enter board size :")
    try:
        board_size = int(input())
        if board_size < 3:
            board_size = 3
            print("Minimum board size is 3. Defaulting to 3x3.")
    except ValueError:
        board_size = 3
        print("Invalid input. Defaulting to 3x3.")

    board = initial_state()
    ai_turn = False
    print(board)

    print("Choose your player (X or 0):")
    user = input().upper()

    if user == "X":
        ai = "0"
    else:
        ai = "X"

    while True:
        game_over = terminal(board)
        current_player = player(board)

        if game_over:
            win = winner(board)
            if win is None:
                print("Game Over: Tie.")
            else:
                print(f"Game Over: {win} wins.")
            break
        else:
            # AI's turn
            if current_player == ai and not game_over:
                move = minimax(board)
                board = result(board, move)
                print("AI moved:")
                print(numpy.array(board))

            # User's turn
            elif current_player == user and not game_over:
                print("Enter the position to move (row,col)")
                try:
                    i = int(input("Row (0-%d): " % (board_size - 1)))
                    j = int(input("Col (0-%d): " % (board_size - 1)))
                    if (i, j) in actions(board):
                        board = result(board, (i, j))
                        print(numpy.array(board))
                    else:
                        print("Invalid move, try again.")
                except ValueError:
                    print("Invalid input, enter numbers only.")
