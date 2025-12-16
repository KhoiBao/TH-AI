import copy
import math
import random
import numpy
X = &quot;X&quot;
O = &quot;O&quot;
EMPTY = None
user = None
ai = None
def initial_state():
&quot;&quot;&quot;
Returns starting state of the board.
&quot;&quot;&quot;
return [[EMPTY, EMPTY, EMPTY],
[EMPTY, EMPTY, EMPTY],
[EMPTY, EMPTY, EMPTY]]
def player(board):
&quot;&quot;&quot;
Returns player who has the next turn on a board.
&quot;&quot;&quot;
count = 0
for i in board:
for j in i:
if j:
count += 1
if count % 2 != 0:
return ai
return user
def actions(board):
&quot;&quot;&quot;
Returns set of all possible actions (i, j) available on the board.
&quot;&quot;&quot;
res = set()
board_len = len(board)
for i in range(board_len):
for j in range(board_len):
if board[i][j] == EMPTY:
res.add((i, j))
return res
def result(board, action):
&quot;&quot;&quot;
Returns the board that results from making move (i, j) on the board.
&quot;&quot;&quot;
curr_player = player(board)
result_board = copy.deepcopy(board)
(i, j) = action
result_board[i][j] = curr_player
return result_board
def get_horizontal_winner(board):
# check horizontally
winner_val = None
board_len = len(board)
for i in range(board_len):
winner_val = board[i][0]
for j in range(board_len):
if board[i][j] != winner_val:

BM KHDL&amp;TTNT
winner_val = None
if winner_val:
return winner_val
return winner_val
def get_vertical_winner(board):
# check vertically
winner_val = None
board_len = len(board)
for i in range(board_len):
winner_val = board[0][i]
for j in range(board_len):
if board[j][i] != winner_val:
winner_val = None
if winner_val:
return winner_val
return winner_val
def get_diagonal_winner(board):
# check diagonally
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
&quot;&quot;&quot;
Returns the winner of the game, if there is one.
&quot;&quot;&quot;
winner_val = get_horizontal_winner(board) or get_vertical_winner(board)
or get_diagonal_winner(board) or None
return winner_val
def terminal(board):
&quot;&quot;&quot;
Returns True if game is over, False otherwise.
&quot;&quot;&quot;
if winner(board) != None:
return True
for i in board:
for j in i:
if j == EMPTY:
return False
return True
def utility(board):
&quot;&quot;&quot;
Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
&quot;&quot;&quot;
winner_val = winner(board)
if winner_val == X:
return 1
elif winner_val == O:
return -1
return 0
def maxValue(state):
if terminal(state):
return utility(state)
v = -math.inf
for action in actions(state):
v = max(v, minValue(result(state, action)))
return v
def minValue(state):
if terminal(state):
return utility(state)
v = math.inf
for action in actions(state):
v = min(v, maxValue(result(state, action)))
return v
def minimax(board):
&quot;&quot;&quot;
Returns the optimal action for the current player on the board.
&quot;&quot;&quot;
current_player = player(board)
if current_player == X:
min = -math.inf
for action in actions(board):
check = minValue(result(board, action)) # FIXED
if check &gt; min:
min = check
move = action
else:
max = math.inf
for action in actions(board):
check = maxValue(result(board, action)) # FIXED
if check &lt; max:
max = check
move = action
return move
if __name__ == &quot;__main__&quot;:
board = initial_state()
ai_turn = False
print(&quot;Choose a player&quot;)
user = input()
if user == &quot;X&quot;:
ai = &quot;O&quot;
else:
ai = &quot;X&quot;
while True:
game_over = terminal(board)
playr = player(board)
if game_over:
winner = winner(board)
if winner is None:
print(&quot;Game Over: Tie.&quot;)
else:
print(f&quot;Game Over: {winner} wins.&quot;)
break;
else:
if user != playr and not game_over:
if ai_turn:
move = minimax(board)
board = result(board, move)
ai_turn = False
print(numpy.array(board))
elif user == playr and not game_over:
ai_turn = True
print(&quot;Enter the position to move (row,col)&quot;)
i = int(input(&quot;Row:&quot;))
j = int(input(&quot;Col:&quot;))
if board[i][j] == EMPTY:
board = result(board, (i, j))
print(numpy.array(board))