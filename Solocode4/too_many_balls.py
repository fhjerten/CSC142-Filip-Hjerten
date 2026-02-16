import pygame
from pygame.locals import *
import sys
from Ball import *

#Variables, not to be changed
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
GAME_TIME = 15 #seconds

#for the text on the screen.
def draw_text(surface, text, x, y, color, font_size=24):
    text_font = pygame.font.SysFont(None, font_size)
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Starting up the pygame here.
pygame.init()
window=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock=pygame.time.Clock() # pygame clock frame rate.
click_sound = pygame.mixer.Sound("sounds/boing.wav")
pygame.mixer.music.load("sounds/background.mp3")

# Playing the background music forever, -1 means loops forever.
pygame.mixer.music.play(-1)

balllist = []
score = 0 #start at 0

startTicks=pygame.time.get_ticks() # record when game starts.

lastSeconds = 0

gameOver = False #False at beginning

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # if player clicks on mouse and game is not over
        if event.type == MOUSEBUTTONDOWN and not gameOver:
            for ball in balllist[:]: # m: means copy

                # if mouse hit the ball
                if ball.ballRect.collidepoint(event.pos):
                    balllist.remove(ball) # remove one ball per click
                    score += 1
                    click_sound.play()

    #this for calculating how many seconds have passed since starting.
    seconds = (pygame.time.get_ticks() - startTicks) // 1000
    if seconds > lastSeconds and not gameOver: 
        lastSeconds = seconds
        
        balllist.append(Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)) # add a new ball

    # if game still on
    if not gameOver:
        for ball in balllist:
            ball.update() # tell every ball to move

    if seconds >= GAME_TIME and not gameOver: #game ends after 15 sec.
        gameOver = True
        balllist.clear()

    window.fill(BLACK) 

    #draw all balls
    for ball in balllist:
        ball.draw()

    draw_text(window, f"Score: {score}", 10, 10, WHITE)
    draw_text(window, f"Seconds: {seconds}", 10, 40, WHITE)

    #if gameover
    if gameOver:
        draw_text(window, "GAME OVER!!", 240,200, WHITE, 36)

        #final score
        draw_text(window, f"Final Score: {score}", 230, 240, WHITE, 32)

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND) # Correct frame rate.