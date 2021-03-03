import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CENTER_X = 300
CENTER_Y = 300

WHITE = (255, 255, 255)
GRAY_LIGHT = (240, 240, 240)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLOCKSIZE = 20
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

CLOCK = pygame.time.Clock()
TICK = 20

def main():
    pygame.init()
    pygame.display.set_caption('Snake game')

    game_over=False

    x = CENTER_X
    y = CENTER_Y
    prev_x = 0
    prev_y = 0
    x_change = 0       
    y_change = 0

    pause = False

    SCREEN.fill(WHITE)
    drawGrid()

    while not game_over:
        for event in pygame.event.get():
            pause = False
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCKSIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCKSIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -BLOCKSIZE
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = BLOCKSIZE
                elif event.key == pygame.K_SPACE:
                    if pause == False:
                        x_change = 0
                        y_change = 0
                        pause = True
    
        prev_x = x
        prev_y = y
        x += x_change
        y += y_change

        if x > WINDOW_WIDTH:
            x = 0
        elif x < 0:
            x = WINDOW_WIDTH

        if y > WINDOW_HEIGHT:
            y = 0
        elif y < 0:
            y = WINDOW_HEIGHT

        snake(x, y, prev_x, prev_y)
        pygame.display.update()
        CLOCK.tick(TICK)

    pygame.quit()

    quit()

def snake(x, y, prev_x, prev_y):
    head_rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
    pygame.draw.rect(SCREEN, GREEN, head_rect)

    if (x != prev_x or y != prev_y):
        white_rect = pygame.Rect(prev_x, prev_y, BLOCKSIZE, BLOCKSIZE)
        cell_rect = pygame.Rect(prev_x, prev_y, BLOCKSIZE, BLOCKSIZE)
        pygame.draw.rect(SCREEN, WHITE, white_rect)
        pygame.draw.rect(SCREEN, GRAY_LIGHT, cell_rect, 1)

def drawGrid():
    for x in range(WINDOW_WIDTH // BLOCKSIZE):
        for y in range(WINDOW_HEIGHT // BLOCKSIZE):
            rect = pygame.Rect(x * BLOCKSIZE, y * BLOCKSIZE,
                               BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, GRAY_LIGHT, rect, 1)

main()
