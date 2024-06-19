import pygame
import numpy as np
import random

# first of all, we have to initialize the pygame library, pygame.init() does the work.
pygame.init()

# next we want a window in which the game will be played, so we set the display name and icon of that window.
pygame.display.set_caption("Jindagi ka Khel")
icon = pygame.image.load("sprout.png")
pygame.display.set_icon(icon)

# so since it's in our hand to shape the window/screen, we set some width and height of it.
screen_width = input("enter the width of the grid: ")  
screen_width = int(screen_width)
screen_height = input("enter the height of the grid: ")  
screen_height = int(screen_height)

# as we need a grid, we choose a cell size and divide the dimension of screen to get no. of cells in a row/column
width = 1200
height = 700

cell_size = width // screen_width
limit = cell_size
# so we have set the shape of our screen, the below function is used to make the screen visible or say work
screen = pygame.display.set_mode((width, height))  

# in the game of life, a cell is either alive or dead, to show this we set some colors (R,G,B).
ALIVE = (255, 255, 0)
DEAD = (64, 64, 64)

FPS = 3

clock = pygame.time.Clock()

# So to keep track which cells are alive and dead, to play the game actually we make use of a numpy array that represent cells of the grid as alive or dead, using entries of only 1 or 0.
grid = np.zeros((screen_height, screen_width))

# intialize the game with random state of the cells.
def randomize_grid():
    for i in range(screen_height):
        for j in range(screen_width):
            grid[i][j] = random.randint(0, 1)

# the game has some rules that are based on no. of neighbours of the cell, so the below function calculates no. of neighbours
def neighbours(grid, x, y):
    count = 0 # set the count to zero
    # so for a cell, the neighbours are the eight cells surrounding it, so we have to check only a index before and index after the cell.
    for i in range(-1, 2): 
        for j in range(-1, 2):
            if i == 0 and j == 0:  # for not counting the cell itself
                continue
            if 0 <= x + i < screen_height and 0 <= y + j < screen_width:
                count += grid[x + i][y + j] # increment the count everytime a neighbouring cell is alive
    return count

# we need to draw the grid and for that we use the pygame.Rect to make rectangle and pygame.draw to show it in screen
def draw_grid():
    for x in range(screen_height):
        for y in range(screen_width):
            rect = pygame.Rect(y * cell_size, x * cell_size, cell_size, cell_size)
            # so if the matrix is valued 1 here, the cell will be alive otherwise dead
            color = ALIVE if grid[x][y] else DEAD
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (40, 40, 40), rect, 1)  # Grid lines

# we want to play the game right? so using the rules we have to update the grid, the following function does that.
def update_grid():

    new_grid = grid.copy() # the game of life proceeds by applying the rules to every cell once based on original grid
    for i in range(screen_height):
        for j in range(screen_width):
            alive_neighbours = neighbours(grid, i, j)
            if grid[i][j] == 1:
                if alive_neighbours < 2 or alive_neighbours > 3:
                    new_grid[i][j] = 0
            else:
                if alive_neighbours == 3:
                    new_grid[i][j] = 1
    return new_grid

def draw_counter(screen, counter):
# Draws the generation counter on the Pygame screen.
    font = pygame.font.Font(None, 36)
    text = font.render(f"Generation: {counter}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

def restart():
    for i in range(screen_height):
        for j in range(screen_width):
            grid[i][j] = 0

pattern = np.array([
    [1,1,1],
    [1,0,1],
    [1,0,1],
])
def make_pattern():
    for l in range(3):
        for p in range(3):
            grid[grid_x+l][grid_y+p] = pattern[l][p]

glider_g = np.array([
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
])

def make_glider_g():
    for l in range(9):
        for p in range(12):
            grid[grid_x+l][grid_y+p] = glider_g[l][p]

pulsar = np.array([
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0]
])
def make_pulsar():
    for l in range(13):
        for p in range(14):
            grid[grid_x+l][grid_y+p] = pulsar[l][p]


kickback_180 = np.array([
    [0,1,0],
    [1,0,0],
    [1,1,1],
    [0,0,0],
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [0,0,1]
])

def make_kickback():
    for l in range(8):
        for p in range(3):
            grid[grid_x+l][grid_y+p] = kickback_180[l][p]

running = True            # stores the state of the game loop
simulation_running = False # stores the state of game, wheter the updation is going on or paused.
single_step = False
generation_counter = 0
one_behind = grid.copy()
goback = 0
behind = np.zeros([1000,screen_height,screen_width])
# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()     # gets the position of mouse click, so the user can set the cells to be alive or dead before simulation or between when it is paused.
            grid_x, grid_y = y // cell_size, x // cell_size 
            grid[grid_x][grid_y] = 1 if grid[grid_x][grid_y] == 0 else 0
            if event.button == 4:
                cell_size+=1
            elif event.button == 5:
                if(cell_size>limit): cell_size+=-1
                else: continue
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                single_step = True
            if event.key == pygame.K_LEFT:
                goback = True   
            elif event.key == pygame.K_SPACE:
                simulation_running = not simulation_running
            elif event.key == pygame.K_r:
                randomize_grid()
            elif event.key == pygame.K_UP:
                cell_size+=1
            elif event.key == pygame.K_DOWN:
                if(cell_size>limit): cell_size+=-1
                else: continue
            elif event.key == pygame.K_z:
                generation_counter=0
                restart()
            elif event.key == pygame.K_1:
                make_kickback()
            elif event.key == pygame.K_2:
                make_pulsar()
            elif event.key == pygame.K_3:
                make_pattern()
            elif event.key == pygame.K_4:
                make_glider_g()

    if goback:
        if(generation_counter): generation_counter +=-1
        grid = behind[generation_counter]
        goback = False  

    if simulation_running or single_step:
        one_behind = grid
        behind[generation_counter] = grid
        grid = update_grid()
        generation_counter +=1
        single_step = False
     
    screen.fill((64, 64, 64))
    draw_grid()
    draw_counter(screen, generation_counter)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()