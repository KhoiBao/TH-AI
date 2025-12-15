import os
import math
from typing import List, Union,Literal
BoardCell = Union[int, Literal["X","O"]]

# --- Hàm kiểm tra người thắng ---
def GetWinner(board):
    """
    Trả về người thắng trên bảng hiện tại nếu có, ngược lại trả về None.
    Bảng (board) là một danh sách 9 phần tử.
    """
    # Định nghĩa tất cả các tổ hợp chiến thắng (hàng, cột, đường chéo)
    winning_combinations = [
        # Hàng ngang
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # Hàng dọc
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # Đường chéo
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        # Kiểm tra xem 3 ô có cùng một giá trị (và không phải là số chỉ ô trống)
        if board[a] == board[b] == board[c] and (board[a] == "X" or board[a] == "O"):
            return board[a]
    
    return None

# --- Hàm in bảng ---
def PrintBoard(board):
    """
    Xóa console và in bảng hiện tại.
    """
    # Lệnh xóa màn hình (cls cho Windows, clear cho Linux/macOS)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Chuyển đổi các số thành chuỗi để in
    display_board = [str(cell) for cell in board]
    
    print(f'''
  {display_board[0]}|{display_board[1]}|{display_board[2]}
  -----
  {display_board[3]}|{display_board[4]}|{display_board[5]}
  -----
  {display_board[6]}|{display_board[7]}|{display_board[8]}
    ''')

# --- Hàm lấy các ô trống ---
def GetAvailableCells(board):
    """
    Trả về một danh sách các chỉ số (1-9) chứa tất cả các ô trống trên bảng.
    """
    available = []
    for cell in board:
        # Ô trống là ô có giá trị là số (1-9), không phải "X" hoặc "O"
        if cell != "X" and cell != "O":
            # Giá trị ô là số từ 1-9
            available.append(cell)
    return available

# --- Thuật toán Minimax với Cắt tỉa Alpha-Beta ---
def minimax(position, depth, alpha, beta, isMaximizing):
    """
    Thuật toán Minimax để xác định giá trị tốt nhất của một nước đi.
    
    :param position: Trạng thái hiện tại của bảng (list).
    :param depth: Độ sâu hiện tại trong cây trò chơi.
    :param alpha: Giá trị tốt nhất mà Maximizer đã tìm thấy cho đến nay.
    :param beta: Giá trị tốt nhất mà Minimizer đã tìm thấy cho đến nay.
    :param isMaximizing: True nếu là lượt của người chơi Maximizing ("X"), False nếu là Minimizing ("O").
    :return: Giá trị đánh giá của trạng thái bảng.
    """
    # 1. Kiểm tra trạng thái kết thúc (người thắng hoặc hòa)
    winner = GetWinner(position)
    if winner != None:
        # Ưu tiên chiến thắng ở độ sâu thấp hơn và thua ở độ sâu cao hơn
        return 10 - depth if winner == "X" else -10 + depth
    
    if len(GetAvailableCells(position)) == 0:
        return 0 # Hòa
    
    # 
    
    # 2. Lượt của Maximizer (Player "X")
    if isMaximizing:
        maxEval = -math.inf
        # Lặp qua tất cả các nước đi có thể
        for cell in GetAvailableCells(position):
            # Thực hiện nước đi
            # Lưu ý: Các ô trống được lưu trữ là số 1-9, nên cần dùng index cell - 1
            position[cell - 1] = "X"
            
            # Gọi đệ quy cho lượt của Minimizer
            Eval = minimax(position, depth + 1, alpha, beta, False)
            
            # Cập nhật giá trị tối đa
            maxEval = max(maxEval, Eval)
            alpha = max(alpha, Eval) # Cập nhật alpha
            
            # Hoàn tác nước đi (trả lại ô trống là số)
            position[cell - 1] = cell 
            
            # Cắt tỉa Alpha-Beta
            if beta <= alpha:
                break 
        return maxEval
    
    # 3. Lượt của Minimizer (Player "O")
    else:
        minEval = +math.inf
        # Lặp qua tất cả các nước đi có thể
        for cell in GetAvailableCells(position):
            # Thực hiện nước đi
            position[cell - 1] = "O"
            
            # Gọi đệ quy cho lượt của Maximizer
            Eval = minimax(position, depth + 1, alpha, beta, True)
            
            # Cập nhật giá trị tối thiểu
            minEval = min(minEval, Eval)
            beta = min(beta, Eval) # Cập nhật beta
            
            # Hoàn tác nước đi
            position[cell - 1] = cell
            
            # Cắt tỉa Alpha-Beta
            if beta <= alpha:
                break 
        return minEval

# --- Hàm tìm nước đi tốt nhất ---
def FindBestMove(currentPosition, AI):
    """
    Tìm nước đi tối ưu cho AI bằng thuật toán Minimax.
    """
    # Thiết lập giá trị ban đầu tùy thuộc AI là Maximizer ("X") hay Minimizer ("O")
    if AI == "X":
        bestVal = -math.inf
        is_maximizing = True
    else:
        bestVal = +math.inf
        is_maximizing = False
        
    bestMove = -1
    
    # Lặp qua tất cả các nước đi có thể
    for cell in GetAvailableCells(currentPosition):
        # Thực hiện nước đi
        currentPosition[cell - 1] = AI
        
        # Gọi Minimax. Lượt tiếp theo sẽ là người chơi ngược lại.
        # Nếu AI là "X" (Maximizing), lượt tiếp theo là Minimizing (False).
        # Nếu AI là "O" (Minimizing), lượt tiếp theo là Maximizing (True).
        next_is_maximizing = not is_maximizing
        
        moveVal = minimax(currentPosition, 0, -math.inf, +math.inf, next_is_maximizing)
        
        # Hoàn tác nước đi
        currentPosition[cell - 1] = cell
        
        # Cập nhật nước đi tốt nhất
        if is_maximizing: # AI là "X" (Maximizer)
            if moveVal > bestVal:
                bestMove = cell
                bestVal = moveVal
        else: # AI là "O" (Minimizer)
            if moveVal < bestVal:
                bestMove = cell
                bestVal = moveVal
                
    return bestMove

# --- Hàm chính của trò chơi ---
def main():
    # 1. Thiết lập trò chơi
    player = input("Chơi với vai trò X hay O? (X/O) ").strip().upper()
    if player not in ("X", "O"):
        print("Lựa chọn không hợp lệ. Mặc định chơi với vai trò X.")
        player = "X"
        
    AI = "O" if player == "X" else "X"
    
    # Bảng trò chơi ban đầu (danh sách các số 1-9)
    currentGame: List[BoardCell] = list(range(1, 10))
    
    # X luôn bắt đầu trước
    currentTurn = "X"
    counter = 0 # Đếm số nước đi
    
    print(f"\nBạn là **{player}**. Máy tính (AI) là **{AI}**.")
    print("Các ô được đánh số từ 1 đến 9.")
    
    # 2. Vòng lặp trò chơi
    while True:
        # A. Lượt của AI
        if currentTurn == AI:
            print(f"\nLượt của AI ({AI}). Đang tính toán nước đi tốt nhất...")
            
            # Lưu ý: Nếu AI là "X" (người bắt đầu), nó luôn chọn ô 1, 3, 7, hoặc 9. 
            # Ô 1 là tốt nhất vì nó đơn giản nhất. Để tối ưu tốc độ, có thể đặt nước đi đầu tiên
            # nhưng ở đây ta vẫn gọi FindBestMove để giữ tính tổng quát.
            
            cell = FindBestMove(currentGame, AI)
            currentGame[cell - 1] = AI
            currentTurn = player # Chuyển lượt sang người chơi
            
        # B. Lượt của người chơi (Human)
        elif currentTurn == player:
            PrintBoard(currentGame)
            
            while True:
                try:
                    humanInput = int(input(f"Nhập số ô bạn muốn đánh ({player}): ").strip())
                except ValueError:
                    PrintBoard(currentGame)
                    print("Lỗi: Vui lòng chỉ nhập số.")
                    continue
                
                # Kiểm tra xem ô có hợp lệ và còn trống không
                if 1 <= humanInput <= 9 and humanInput in currentGame:
                    currentGame[humanInput - 1] = player
                    currentTurn = AI # Chuyển lượt sang AI
                    break
                else:
                    PrintBoard(currentGame)
                    print("Lỗi: Ô không hợp lệ hoặc đã được đánh. Vui lòng thử lại.")

        # C. Kiểm tra kết thúc trò chơi
        winner = GetWinner(currentGame)
        if winner != None:
            PrintBoard(currentGame)
            print(f"\n*** {winner} ĐÃ THẮNG!!! ***")
            break
            
        counter += 1
        # Nếu không có người thắng và bảng đã đầy (9 nước đi)
        if counter == 9:
            PrintBoard(currentGame)
            print("\n*** HÒA! ***")
            break

# --- Điểm khởi động ---
if __name__ == "__main__":
    main()