import math
import copy
import random
import tkinter as tk
from tkinter import messagebox

# Declare constants
X = "X"
O = "0"
EMPTY = None 
user = None
ai = None
board_size = 3
win_length = 3  # number in a row needed to win
MAX_DEPTH = 4   # AI search depth limit


# Initialize the starting state of the board
def initial_state():
    return [[EMPTY for _ in range(board_size)] for _ in range(board_size)]


# Determine whose turn it is
def player(board):
    count = sum(cell is not EMPTY for row in board for cell in row)
    return ai if count % 2 else user


# Possible moves
def actions(board):
    result = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                result.add((i, j))
    return result


# Apply a move to a board
def result(board, action): 
    current_player = player(board)
    new_board = copy.deepcopy(board)
    (i, j) = action
    new_board[i][j] = current_player
    return new_board


# ---------- WIN CHECKS WITH WIN LENGTH ---------- #

def check_sequence(seq):
    """Check if there's a winning streak of length `win_length` in a sequence."""
    global win_length
    for i in range(len(seq) - win_length + 1):
        segment = seq[i:i+win_length]
        if segment[0] is not EMPTY and all(cell == segment[0] for cell in segment):
            return segment[0]
    return None


def check_horizontal_winner(board):
    for row in board:
        result = check_sequence(row)
        if result:
            return result
    return None


def check_vertical_winner(board):
    n = len(board)
    for col in range(n):
        column = [board[row][col] for row in range(n)]
        result = check_sequence(column)
        if result:
            return result
    return None


def check_diagonal_winner(board):
    n = len(board)

    # Diagonals (top-left to bottom-right)
    for i in range(n - win_length + 1):
        for j in range(n - win_length + 1):
            diag = [board[i + k][j + k] for k in range(min(n - i, n - j))]
            result = check_sequence(diag)
            if result:
                return result

    # Diagonals (top-right to bottom-left)
    for i in range(n - win_length + 1):
        for j in range(win_length - 1, n):
            diag = [board[i + k][j - k] for k in range(min(n - i, j + 1))]
            result = check_sequence(diag)
            if result:
                return result

    return None


def winner(board):
    return check_horizontal_winner(board) or check_vertical_winner(board) or check_diagonal_winner(board)


def terminal(board):
    if winner(board) is not None:
        return True
    return all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0


# ---------- ALPHA-BETA MINIMAX ---------- #

def maxValue(state, alpha, beta, depth=0):
    if terminal(state) or depth >= MAX_DEPTH:
        return utility(state)
    v = -math.inf
    for action in actions(state):
        v = max(v, minValue(result(state, action), alpha, beta, depth + 1))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def minValue(state, alpha, beta, depth=0):
    if terminal(state) or depth >= MAX_DEPTH:
        return utility(state)
    v = math.inf
    for action in actions(state):
        v = min(v, maxValue(result(state, action), alpha, beta, depth + 1))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v


def minimax(board):
    current_player = player(board)
    all_actions = list(actions(board))

    # Fallback: random move if board too large
    if len(all_actions) > 9 and len(board) > 3:
        return random.choice(all_actions)

    move = None
    if current_player == X:
        best_val = -math.inf
        for action in all_actions:
            val = minValue(result(board, action), -math.inf, math.inf)
            if val > best_val:
                best_val = val
                move = action
    else:
        best_val = math.inf
        for action in all_actions:
            val = maxValue(result(board, action), -math.inf, math.inf)
            if val < best_val:
                best_val = val
                move = action
    return move


# ---------- GUI ---------- #

def update_board_buttons():
    for i in range(board_size):
        for j in range(board_size):
            text = board[i][j] if board[i][j] else ""
            buttons[i][j].config(text=text, state="disabled" if board[i][j] else "normal")


def make_move(i, j):
    global board
    if board[i][j] is EMPTY:
        board[i][j] = user
        update_board_buttons()

        if terminal(board):
            end_game()
            return

        ai_move = minimax(board)
        if ai_move:
            board = result(board, ai_move)
            update_board_buttons()

        if terminal(board):
            end_game()


def end_game():
    win = winner(board)
    if win is None:
        messagebox.showinfo("Game Over", "It's a tie!")
    else:
        messagebox.showinfo("Game Over", f"{win} wins!")
    root.destroy()


# ---------- MAIN GAME ---------- #

def start_game():
    global user, ai, board_size, win_length, board, buttons, root
    user = user_choice.get()
    ai = O if user == X else X
    board_size = int(size_choice.get())
    win_length = int(win_choice.get())

    if win_length > board_size:
        messagebox.showerror("Error", "Win length cannot exceed board size!")
        return

    board = initial_state()

    root = tk.Tk()
    root.title(f"Tic-Tac-Toe {board_size}x{board_size} (Win {win_length})")

    buttons = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            btn = tk.Button(root, text="", width=5, height=2, font=("Arial", 16),
                            command=lambda i=i, j=j: make_move(i, j))
            btn.grid(row=i, column=j, padx=3, pady=3)
            row.append(btn)
        buttons.append(row)

    update_board_buttons()
    root.mainloop()


# ---------- MENU ---------- #

menu = tk.Tk()
menu.title("Game Setup")

tk.Label(menu, text="Choose Player:").grid(row=0, column=0, padx=5, pady=5)
user_choice = tk.StringVar(value="X")
tk.Radiobutton(menu, text="X", variable=user_choice, value="X").grid(row=0, column=1)
tk.Radiobutton(menu, text="0", variable=user_choice, value="0").grid(row=0, column=2)

tk.Label(menu, text="Board Size:").grid(row=1, column=0, padx=5, pady=5)
size_choice = tk.StringVar(value="3")
tk.Entry(menu, textvariable=size_choice, width=5).grid(row=1, column=1)

tk.Label(menu, text="Win Length:").grid(row=2, column=0, padx=5, pady=5)
win_choice = tk.StringVar(value="3")
tk.Entry(menu, textvariable=win_choice, width=5).grid(row=2, column=1)

tk.Button(menu, text="Start Game", command=start_game, bg="#4CAF50", fg="white").grid(row=3, column=0, columnspan=3, pady=10)

menu.mainloop()
