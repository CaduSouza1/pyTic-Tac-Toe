import board

b = [
    [board.BoardCell.PLAYER_O,board.BoardCell.PLAYER_X,board.BoardCell.PLAYER_X],
    [board.BoardCell.PLAYER_O,board.BoardCell.EMPTY,board.BoardCell.EMPTY],
    [board.BoardCell.PLAYER_O,board.BoardCell.EMPTY,board.BoardCell.EMPTY]
]

print(board.CheckPlayerWon(board.BoardCell.PLAYER_O, b))