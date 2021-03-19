
import render
import pygame
import board
import sys

pygame.init()


screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

current_turn = board.BoardCell.PLAYER_X

row_count, colum_count = 3, 3
game_board = [
    [board.BoardCell.EMPTY for row in range(0, row_count)] for colum in range(0, colum_count)
]

cell_width = screen.get_width() // len(game_board[0])
cell_height = screen.get_height() // len(game_board)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row, colum = board.GetMouseCell(mouse_x, mouse_y, cell_width, cell_height)
            game_board[row][colum] = current_turn

            if board.CheckPlayerWon(current_turn, game_board):
                sys.exit()

            current_turn = (current_turn + 1) % len(board.BoardCell)
            if current_turn == board.BoardCell.EMPTY:
                current_turn += 1

    screen.fill((0, 0, 0))
    render.DrawBoard(screen, cell_width, cell_height, game_board, (255, 255, 255))
    pygame.display.update()

pygame.quit()
