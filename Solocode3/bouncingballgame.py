import pygame
from pygame.locals import *
import sys
import random

#Constants, not to be changed
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3
MAX_SCORE = 5

#The text function to get the text on the screen
def draw_text(surface, text, x, y, color, font_size=24, center=False):
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect()

    # for putting the text in the center down here. 
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(text_surface, rect)    


# Setting up the pygame here.
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Loading sound effect and backgorund music.
pygame.mixer.music.load("sounds/background.mp3")
pygame.mixer.music.play(-1)  # Play background music in a loop

boing_sound = pygame.mixer.Sound("sounds/boing.wav")    # "When ball is clicked on" sound.

# The ball image.
ball_image = pygame.image.load("images/ball.png")

# The ball's position will be random.
ballRect = ball_image.get_rect()
ballRect.left = random.randrange(WINDOW_WIDTH - ballRect.width)
ballRect.top = random.randrange(WINDOW_HEIGHT - ballRect.height)

# the original speed of ball on x and y axis.
xspeed = N_PIXELS_PER_FRAME
yspeed = N_PIXELS_PER_FRAME

# the variables in the game.
start_time = pygame.time.get_ticks()  # recording the start time
score = 0    # startinng score is 0
game_over = False


#Main Game loop that runs forever

while True:

    for event in pygame.event.get():
        # If press close, the game closes.
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # if clicked with mouse button
        if event.type == MOUSEBUTTONDOWN and not game_over:
            # Checking if the mouseclick was on the ball.
            if ballRect.collidepoint(event.pos):
                score += 1
                boing_sound.play()

                #reseting the ball to new positon if clicked on.
                ballRect.left = random.randrange(WINDOW_WIDTH - ballRect.width)
                ballRect.top = random.randrange(WINDOW_HEIGHT - ballRect.height)

                # Increase ball speed if clicked every time
                xspeed = abs(xspeed) + random.randint(1, 5)
                yspeed = abs(yspeed) + random.randint(1, 5)

                # random direction for ball if clicked
                if random.choice([True, False]):
                    xspeed = -xspeed
                if random.choice([True, False]):
                    yspeed = -yspeed

                # the game ends after 5 points.
                if score == MAX_SCORE:
                    game_over = True
                    end_time = pygame.time.get_ticks()
                    total_time = (end_time - start_time) / 1000  # 1000 milliseconds = 1 second

    # only moving ball if game is on.            
    if not game_over:
        ballRect.left += xspeed
        ballRect.top += yspeed

        # this makes the ball go in the opposite direction of the wall it hits.
        if ballRect.left < 0 or ballRect.right > WINDOW_WIDTH:
            xspeed = -xspeed    
        if ballRect.top < 0 or ballRect.bottom > WINDOW_HEIGHT:
            yspeed = -yspeed

# draw everything in a tiny screen.
    window.fill(BLACK)
    draw_text(window, f"Score: {score}", 10, 10, WHITE)

    if not game_over:
        window.blit(ball_image, ballRect)
    else:
        draw_text(        # showing all this when the game is over and you win it.
            window,
            f"Game finished in {total_time:.2f} seconds!",  # .2f gives the total time 2 decimals to it.
            center = True,
            x = WINDOW_WIDTH // 2,
            y = WINDOW_HEIGHT // 2,
            color = WHITE
        )
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
