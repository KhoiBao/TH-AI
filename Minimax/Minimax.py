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
# assume that flag = X and O is player 


# Initialize the starting state of the board
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Create player role
def player(board):
    count = 0
    for i in board:
        for j in i:
                if j:
                    count += 1
                    if count  % 2 != 0: # shadowing the state that user is always the first players
                        return ai 
                    return user 

# represent actions has been made
def actions(board):
    result = set() 
    
    board_length = len(board) # get the whole board, row x column.
    
    for i in range(board_length): # column index (regconize the flag that stayed on row or diagonal space and save into result).
        
        for j in range(board_length): # row index (regconize the flag that stayed on row or vertical space and save into result).
            
            if board[i][j] == EMPTY: 
                
                result.add((i,j))
                
    return result
move = actions
def result(board, action): 
    current_player = player(board)# the player(board) is dedicate in return which turn is it on the board, therefore we need to appoint it to another mask that based on what does the player(board) given
    
    result_board = copy.deepcopy(board)
    
    (i,j) = action
    
    result_board[i][j] = current_player
    
    return result_board

# check phuong ngang
def check_horizontal_winner(board): 

    winner_val = None # initial the winner value
    
    board_length = len(board) # length or size of the board

    for i in range(board_length): # repeat through every single row

        winner_val = board[i][0] # IF the winner is in the first box (1)

        for j in range(board_length): # begin repeat going through the (i) row(horizontal) on the j (vertical)

            if board[i][j] != winner_val: # if there is no winning flag (2)
                winner_val = None # return none (2)

            if winner_val: # then if its in whether the j range of movement
                return winner_val # give back the winner value
            
    return winner_val # (1) then return the winner value

# check phuong doc
def check_vertical_winner(board): 
    winner_val = None # initial the winner value

    board_length = len(board) # length or size of the board

    for i in range(board_length): # repeat through every single column

        winner_val = board[0][i] # IF the winner is in the first box (1)

        for j in range(board_length): # begin repeat 

            if board[j][i] != winner_val: # check on vertical
                winner_val = None

        if winner_val:

            return winner_val
        
        winner_val = board[0][board_length - 1]

        for i in range(board_length):

            j = board_length - 1 - i

            if board[i][j] != winner_val:

                winner_val = None

        return winner_val
    
    return winner_val #(1) then return the winner value
        

# Check phuong cheo
def check_diagonal_winner(board): 
    
    winner_val = None # not admitting winner yet therefore gave it as None
    
    board_len = len(board) # length of the board
    
    winner_val = board[0][0] # assumed that the winner is on the first element of the board
    
    for i in range(board_len):
        
        if board[i][i] != winner_val: # if the winner isn't at the first element of the board
            
            winner_val = None # there is no winner
        
        if winner_val: # IF the winner is actually at the first element

            return winner_val # return to user the value of the winner
        
        winner_val = board[0][board_len - 1]
        
        for i in range(board_len):

            j = board_len - 1 - i
        
            if board[i][j] != winner_val:

                winner_val = None

        return winner_val
    
def winner(board):
# Returns the winner of the game, if there is one
    winner_val = check_horizontal_winner(board) or check_vertical_winner(board) or check_diagonal_winner(board) or None 

    return winner_val

def terminal(board):
#Returns True if game is over, False otherwise.
    if winner(board) != None:

        return True
    
    for i in board:

        for j in i:

            if j == EMPTY:

                return False
            
    return True

def utility(board): # Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    winner_val = winner(board)

    if winner_val == X:

        return 1
    
    elif winner_val == O:

        return -1
    
    return 0

# MAX function, represent for AI

def maxValue(state): # give out state as a dummy to represent board score
    
    if terminal(state): 

        return utility(state) # add or minus depended on function utility(board)
    
    v = -math.inf # Max need to be as small as possible due to "Maximize"

    for action in actions(state):

        v = max(v, minValue(result(state, action)))
            
    return v

# MIN function, represent for Player
def minValue(state):

    if terminal(state):

        return utility(state)
    
    v = math.inf
    
    for action in actions(state):

        v = min(v, maxValue(result(state, action)))

    return v

#Returns the optimal action for the current player on the board.
def minimax(board):
    current_player = player(board)

    if current_player == X:
        min = -math.inf
        move = None
        for action in actions(board):
            check = minValue(result(board, action))
            if check > min:
                min = check
                move = action
    else:
        max = math.inf
        move = None
        for action in actions(board):
            check = maxValue(result(board, action))
            if check < max:
                best_val = check
                move = action
    return move
if __name__ == "__main__":
    board = initial_state()
    ai_turn = False

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
                    i = int(input("Row (0-2): "))
                    j = int(input("Col (0-2): "))
                    if (i, j) in actions(board):
                        board = result(board, (i, j))
                        print(numpy.array(board))
                    else:
                        print("Invalid move, try again.")
                except ValueError:
                    print("Invalid input, enter numbers 0-2.")
