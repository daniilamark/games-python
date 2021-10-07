# pip install pygame
import pygame
from random import randrange

RES = 680  # dimension of a square window
SIZE = 40  # size of sections

# random initial position of the snake and the apple
# from the resolution range in increments of size
x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

dirs = {'W': True, 'S': True, 'A': True, 'D': True}  # dictionary of permitted movements
length = 1  # snake length
snake = [(x, y)]  # a snake in the form of a list of coordinates
dx, dy = 0, 0  # direction of movement
fps = 5  # snake speed
score = 0
Icon = pygame.image.load('../img/snake_ico.png')

pygame.display.set_icon(Icon)

pygame.init()
pygame.display.set_caption('Game Snake')

sc = pygame.display.set_mode([RES, RES])  # creating a working window
clock = pygame.time.Clock()  # to regulate the speed of the snake

# defining fonts
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 120, bold=True)

img = pygame.image.load('../img/bg.jpg').convert()

while True:
    # sc.fill(pygame.Color('black'))
    sc.blit(img, (0, 0))

    # drawing snake, apple
    # using list inclusion
    [(pygame.draw.rect(sc, pygame.Color('green'), pygame.Rect(i, j, SIZE - 2, SIZE - 2), 50, 10)) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), pygame.Rect(*apple, SIZE, SIZE), 50, 10)

    # show score
    render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))

    # snake movement
    # one step is equal to the size of the head
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))  # adding snake steps to the list of coordinates
    snake = snake[-length:]  # a slice of coordinates

    # eating apple
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1
        fps += 1

    # game over
    # going out of bounds and eating yourself
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', True, pygame.Color('orange'))
            sc.blit(render_end, (RES // 2 - 300, RES // 2.5))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()  # updating the surface
    clock.tick(fps)  # delay for fps

    # checking the closing of the application
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # control
    key = pygame.key.get_pressed()

    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
