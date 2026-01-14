import pygame, random

BOARD_ROWS = 16
BOARD_COLS = 20

WIDTH = 640
HEIGHT = 512
#test

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whack-A-Mole")

SQUARE_SIZE = 32

GRID_COLOR = (128, 0, 128) # purple
GRID_WIDTH = 1
BACKGROUND_COLOR = (159, 43, 104) #amaranth

mole_image = pygame.image.load("mole.png")

def initialize_board():
    board =[["-"for i in range(BOARD_COLS)] for j in range(BOARD_ROWS)]
    return board

def random_position():
    x = random.randrange(0, 20)
    y = random.randrange(0, 16)
    return x, y

def mole_position(row, col):
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if (row == i) and (col == j):
                board[i][j] = 'x'
            else:
                board[i][j] = '-'
    return board

def get_mole_postition(board):
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if (board[i][j] == 'x'):
                return i, j

def print_board(board):
    print()
    for row in board:
        for col_num, col in enumerate(row):
            if col_num == len(row)-1:
                print(col, end='')
            else:
                print(col, end=' ')
        print()
    print()

def draw_grids():
    # draw horizontal grids
    for i in range(BOARD_ROWS):
        pygame.draw.line(screen, GRID_COLOR, (0, SQUARE_SIZE*i), (WIDTH, SQUARE_SIZE*i), GRID_WIDTH)
    # draw vertical grids
    for i in range(BOARD_COLS):
        pygame.draw.line(screen, GRID_COLOR, (SQUARE_SIZE*i, 0), (SQUARE_SIZE*i, HEIGHT), GRID_WIDTH)

def draw_mole():
    col, row = random_position()
    screen.blit(mole_image, mole_image.get_rect(center=(col*SQUARE_SIZE+SQUARE_SIZE/2, row*SQUARE_SIZE+SQUARE_SIZE/2)))
    mole_position(row, col)
    print_board(board)
    

screen.fill(BACKGROUND_COLOR)
draw_grids()
board = initialize_board()

screen.blit(mole_image, mole_image.get_rect(topleft=(0,0)))
mole_position(0,0)
print_board(board)


def main():
    try:
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    row = y // SQUARE_SIZE
                    col = x // SQUARE_SIZE

                    # get mole position
                    mole_pos_y, mole_pos_x = get_mole_postition(board)

                    if (col == mole_pos_x) and (row == mole_pos_y):
                        screen.fill(BACKGROUND_COLOR)
                        draw_grids()
                        draw_mole()

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
