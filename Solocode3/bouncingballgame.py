import pygame
from pygame.locals import *
import sys
import random

#Constants, not to be changed
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

# Setting up the pygame window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Images, sounds etc.
ball_image = pygame.image.load("images/ball.png")

# The ball's position will be random.
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.RECT(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT) # limits for the ball

#Main Game loop
while True:
    for event in pygame.event.get():
        # If press close, the game closes.
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # if clicked with mouse button
        if event.type == pygame.MOUSEBUTTONUP:

            # Checking if the mouseclick was on the ball.
            if ballRect.collidepoint(event.pos):
                #Moving the ball to new positon if clicked on.
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.RECT(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    
    # Drawing the whole game
    window.fill(BLACK)

    window.blit(ball_image, (ballX, ballY)) # Adding the ball.

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)





