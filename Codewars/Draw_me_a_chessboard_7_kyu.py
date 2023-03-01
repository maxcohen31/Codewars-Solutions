from typing import List
def chess_board(rows: int, columns: int) -> List[List[str]]:
    board = []
    result = []
    for i in range(rows):
        for j in range(columns):
            if i % 2 == 0:
                if j % 2 == 0:
                    board.append('O')
                else:
                    board.append('X')
            elif i % 2 != 0:
                if j % 2 != 0:
                    board.append('O')
                else:
                    board.append('X')
    for b in range(0, len(board), columns):
        result.append(board[b:b+columns])
    return result





print(chess_board(6, 4)) 
""" [
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"]
] 
"""