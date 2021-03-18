from typing import List, Tuple


class BoardCell:
    EMPTY = 0
    PLAYER_X = 1
    PLAYER_O = 2


def GetMouseCell(mouse_x: int, mouse_y: int, cell_width: int, cell_height: int) -> Tuple[int, int]:
    row = mouse_x // cell_width
    colum = mouse_y // cell_height

    return (row, colum)


def GetRows(game_board: List[List[BoardCell]]) -> List[BoardCell]:
    return [game_board[row] for row in range(0, len(game_board))]

# TODO: This function doesn't return the columns, it returns the rows
def GetColumns(game_board: List[List[BoardCell]]) -> List[BoardCell]:
    return [game_board[0:len(game_board)][colum] for colum in range(0, len(game_board))]

# TODO: Make the return only use 1 loop
def GetDiagonals(game_board: List[List[BoardCell]]) -> List[BoardCell]:
    return [
        [game_board[i][i] for i in range(0, len(game_board))], # main diagonal
        [game_board[len(game_board) - 1 - i][i] for i in range(0, len(game_board))] # reverse diagonal
    ]


def CheckPlayerWon(player: int, game_board: List[List[BoardCell]]):
    for row in GetRows(game_board):
        if all(map(lambda p: p == player, row)):
            return True
    
    for colum in GetColumns(game_board):
        if all(map(lambda p: p == player, colum)):
            return True
    
    for diagonal in GetDiagonals(game_board):
        if all(map(lambda p: p == player, diagonal)):
            return True

    return False