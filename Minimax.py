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
# assume that flag = X and O


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
            for j in i:
                if j:
                    count += 1
                    if count  % 2 != 0: # shadowing the state that user is always the first players
                        return ai 
                    return user 

# announce the "flag" that has been made on the board
def actions(board):
    result = set() 
    
    board_length = len(board) # get the whole board, row x column.
    
    for i in range(board_length): # column index (regconize the flag that stayed on row or diagonal space and save into result).
        
        for j in range(board_length): # row index (regconize the flag that stayed on row or vertical space and save into result).
            
            if board[i][j] == EMPTY: 
                
                result.add((i,j))
                
                return result

def result(board, action): 
    current_player = player(board)# the player(board) is dedicate in return which turn is it on the board, therefore we need to appoint it to another mask that based on what does the player(board) given
    result_board = copy.deepcopy(board)
    (i,j) = action
    result_board[i][j] = current_player
    return result_board

def check_horizontal_winner(board): # check phuong ngang

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

def check_vertical_winner(board): # check phuong doc
    winner_val = None # initial the winner value

    board_length = len(board) # length or size of the board

    for i in range(board_length): # repeat through every single column
        winner_val = board[0][i] # IF the winner is in the first box (1)

        for j in range(board_length): # begin repeat 
            if board[i][i] != winner_val:
                winner_val = None

        if winner_val:
            return winner_val
        winner_val = board[0][board_length - 1]

        for i in range(board_length):
            j = board_length - 1 - i

        if board[i][j] != winner_val:
            winner_val = None
        return winner_val

def check_diagonal_winner(board):
    winner_val = None
    board_len = len(board)
    winner_val = board[0][0]
    for i in range(board_len):
        if board[i][i] != winner_val:
            winner_val = None
        if winner_val:
            return winner_val
        winner_val = board[0][board_len - 1]
        for i in range(board_len):
            j = board_len - 1 - i
        if board[i][j] != winner_val:
            winner_val = None
        return winner_val
def winner(board):
# Returns the winner of the game, if there is one.
    winner_val = check_horizontal_winner(board) or check_vertical_winner(board) or check_diagonal_winner(board) or None 
    return winner_val

    
