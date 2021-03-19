from typing import List, Tuple
from enum import IntEnum


class BoardCell(IntEnum):
    EMPTY = 0
    PLAYER_X = 1
    PLAYER_O = 2


def GetMouseCell(mouse_x: int, mouse_y: int, cell_width: int, cell_height: int) -> Tuple[int, int]:
    row = mouse_x // cell_width
    colum = mouse_y // cell_height

    return (row, colum)


def GetRows(game_board: List[List[BoardCell]]) -> List[List[BoardCell]]:
    return [row for row in game_board]


def GetColumns(game_board: List[List[BoardCell]]) -> List[List[BoardCell]]:
    columns = []

    for i in range(0, len(game_board)):
        columns.append([row[i] for row in game_board])

    return columns


def GetDiagonals(game_board: List[List[BoardCell]]) -> List[List[BoardCell]]:
    main_diag = []
    reverse_diag = []
    
    for i in range(0, len(game_board)):
        main_diag.append(game_board[i][i])
        reverse_diag.append(game_board[len(game_board) - 1 - i][i])

    return main_diag, reverse_diag

 
def CheckPlayerWon(player: int, game_board: List[List[BoardCell]]) -> Tuple[bool, int]:
    for row in GetRows(game_board):
        if all(map(lambda p: p == player, row)):
            return player
    
    for colum in GetColumns(game_board):
        if all(map(lambda p: p == player, colum)):
            return player
    
    for diagonal in GetDiagonals(game_board):
        if all(map(lambda p: p == player, diagonal)):
            return player

    return 0