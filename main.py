import render
import pygame
import board

num_pass, num_fail = pygame.init()
if num_fail:
    print("Failed to initialize pygame")

should_reset = False


def main():
    global should_reset

    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    player_won = 0
    current_turn = board.BoardCell.PLAYER_X

    row_count, colum_count = 3, 3
    game_board = [
        [board.BoardCell.EMPTY for row in range(0, row_count)] for colum in range(0, colum_count)
    ]

    cell_width = screen.get_width() // len(game_board[0])
    cell_height = screen.get_height() // len(game_board)

    font_obj = pygame.font.Font("8_bit_arcade\8-bit Arcade In.ttf", 30)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN and not player_won:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row, colum = board.GetMouseCell(mouse_x, mouse_y, cell_width, cell_height)
                game_board[row][colum] = current_turn

                player_won = board.CheckPlayerWon(current_turn, game_board)

                current_turn = (current_turn + 1) % len(board.BoardCell)
                if current_turn == board.BoardCell.EMPTY:
                    current_turn += 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    should_reset = True
                    return

        screen.fill((0, 0, 0))
        render.DrawBoard(screen, cell_width, cell_height, game_board, (255, 255, 255))
        if player_won:
            text_size = font_obj.size("You won")
            text_x = screen.get_width() // 2 - text_size[0] // 2
            text_y = screen.get_height() - text_size[1]

            render.BlitText(screen, font_obj, text_x, text_y - text_size[1], "You won", (255, 255, 255))
            render.BlitText(screen, font_obj, text_x, text_y, "Press spacebar to reset", (255, 255, 255))

        pygame.display.update()


main()

if should_reset:
    should_reset = False
    main()

pygame.quit()