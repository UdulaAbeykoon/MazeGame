import pygame
import random

# initialize Pygame
pygame.init()

# define the maze as a 2D list of cells
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

# define the starting and ending positions
start = (1, 1)
end = (8, 8)

# define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# define the screen dimensions
WIDTH = 600
HEIGHT = 600

# create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# define the player position
player = start

# define the game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if maze[player[0]-1][player[1]] != '#':
                    player = (player[0]-1, player[1])
            elif event.key == pygame.K_DOWN:
                if maze[player[0]+1][player[1]] != '#':
                    player = (player[0]+1, player[1])
            elif event.key == pygame.K_LEFT:
                if maze[player[0]][player[1]-1] != '#':
                    player = (player[0], player[1]-1)
            elif event.key == pygame.K_RIGHT:
                if maze[player[0]][player[1]+1] != '#':
                    player = (player[0], player[1]+1)

    # check if the player has reached the end
    if player == end:
        print('Congratulations! You have reached the end of the maze!')
        running = False

    # clear the screen
    screen.fill(BLACK)

    # draw the maze
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == '#':
                pygame.draw.rect(screen, WHITE, (col*60, row*60, 60, 60))
            elif (row, col) == player:
                pygame.draw.rect(screen, GREEN, (col*60, row*60, 60, 60))
            elif (row, col) == end:
                pygame.draw.rect(screen, RED, (col*60, row*60, 60, 60))

    # update the screen
    pygame.display.flip()

   