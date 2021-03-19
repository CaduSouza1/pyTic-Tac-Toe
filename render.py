from typing import List, Tuple
from pygame.surface import Surface
import pygame.draw
import pygame.font
from board import BoardCell


def DrawBoard(surface: Surface, cell_width: int, cell_height: int, game_board: List[List[BoardCell]], bg_color: Tuple[int, int, int]):
    for row in range(0, len(game_board[0])):
        for colum in range(0, len(game_board[row])):
            DrawCellBG(
                surface, cell_width * row, cell_height *
                colum, cell_width, cell_height, bg_color
            )

            if game_board[row][colum] == BoardCell.PLAYER_X:
                margin_x = cell_width // 4
                margin_y = cell_height // 4

                x = cell_width * row + margin_x
                y = cell_height * colum + margin_y

                # counting for the "+ margin" in the x and y initial positions
                line_length_x = cell_width - margin_x * 2
                line_length_y = cell_height - margin_y * 2
                DrawPlayerX(surface, x, y, line_length_x,
                            line_length_y, (255, 0, 0))

            elif game_board[row][colum] == BoardCell.PLAYER_O:
                center_x = cell_width * row + cell_width // 2
                center_y = cell_height * colum + cell_height // 2

                radius = cell_height // 4
                DrawPlayerO(surface, center_x, center_y, radius, (0, 0, 255))


def DrawCellBG(surface: Surface, x: int, y: int, width: int, height: int, color: Tuple[int, int, int]):
    pygame.draw.rect(surface, color, [x, y, width, height], 1)


def DrawPlayerX(surface: Surface, x: int, y: int, line_length_x: int, line_length_y: int, color: Tuple[int, int, int]):
    pygame.draw.line(surface, color, (x, y),
                     (x + line_length_x, y + line_length_y), 10)
    pygame.draw.line(surface, color, (x + line_length_x, y),
                     (x, y + line_length_y), 10)


def DrawPlayerO(surface: Surface, x: int, y: int, radius: int, color: Tuple[int, int, int]):
    pygame.draw.circle(surface, color, (x, y), radius)
    pygame.draw.circle(surface, (0, 0, 0), (x, y), radius - 10)


def BlitText(surface: Surface, font_obj: pygame.font.Font, x: int, y: int, text: str, color: Tuple[int, int, int]):
    surface.blit(
        font_obj.render(text, False, color), 
        (x, y)
    )
