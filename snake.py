import pygame as pg
import random
from sys import exit

WIDTH = 600
HEIGHT = 600

screen = pg.display.set_mode((WIDTH,HEIGHT))
title = pg.display.set_caption('The Snake Game')
clock = pg.time.Clock()

#colors
BACKGROUND_COLOR = 'BLACK'
SNAKE_COLOR = 'LIME'
FOOD_COLOR = 'RED'

TILE_SIZE = 20

pg.font.init()
font = pg.font.SysFont(None, 50)
 
def snake(TILE_SIZE, snakeBody):
    for x in snakeBody:
        pg.draw.rect(screen, SNAKE_COLOR, [x[0], x[1], TILE_SIZE, TILE_SIZE])

def message(msg):
    mesg = font.render(msg, True, 'red')
    screen.blit(mesg, [WIDTH/6, HEIGHT/2])

def gameLoop():
    #coordinates
    x = WIDTH/2
    y = HEIGHT/2

    #holds the coords for the next movement direction
    xCoord = 0
    yCoord = 0

    snakeBody = []

    #initial food placement
    foodx = round(random.randrange(0, WIDTH) // TILE_SIZE) * TILE_SIZE
    foody = round(random.randrange(0, HEIGHT) // TILE_SIZE) * TILE_SIZE

    gameStatus = True

    while True:

        screen.fill(BACKGROUND_COLOR)

        while gameStatus == False:
            message("You Lost! Play again? y/n")
 
            pg.display.update()
 
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_y:
                        gameLoop()
                    if event.key == pg.K_n:
                        pg.quit()
                        exit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    xCoord = -TILE_SIZE
                    yCoord = 0
                elif event.key == pg.K_RIGHT:
                    xCoord = TILE_SIZE
                    yCoord = 0
                elif event.key == pg.K_UP:
                    yCoord = -TILE_SIZE
                    xCoord = 0
                elif event.key == pg.K_DOWN:
                    yCoord = TILE_SIZE
                    xCoord = 0
        
        #new coordinates based on the movement direction of the snake
        x += xCoord
        y += yCoord

        #checks for collisions with the borders of the window.
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            gameStatus = False

        #checks for collision
        for tile in snakeBody[1:]:
            if x == tile[0] and y == tile[1]:
                gameStatus = False

        #controls the length of the snake (adding and removal of tiles in snakebody when moving around)
        snakeBody.append([x,y])
        if len(snakeBody) > 1:
            del snakeBody[0]

        #draws the food and snake on the screen
        pg.draw.rect(screen, FOOD_COLOR, [foodx, foody, TILE_SIZE, TILE_SIZE])
        snake(TILE_SIZE,snakeBody)


        #checks if the snake eats the food item and adds a new bodytile to the snake if so
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, WIDTH) // TILE_SIZE) * TILE_SIZE
            foody = round(random.randrange(0, HEIGHT) // TILE_SIZE) * TILE_SIZE
            snakeBody.append([x,y])

        pg.display.update()
        pg.time.delay(70)
        clock.tick(50)

gameLoop()