import pygame
from pygame.locals import *
import sys
import pygwidgets
from game import *

pygame.init()
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Blacjack GUI")
clock = pygame.time.Clock()

# backgorund image
background = pygwidgets.Image(window, (0, 0), 'images/background.png')

# game buttons
hitButton = pygwidgets.TextButton(window, (300, 520), "Hit", width=120, height=55)
stayButton = pygwidgets.TextButton(window, (500, 520), "Stay", width=120, height=55)
newButton = pygwidgets.TextButton(window, (20, 520), "New Game", width=100, height=45)
quitButton = pygwidgets.TextButton(window, (880, 530), "Quit", width=100, height=45)

game = Game(window)

while True:
    for event in pygame.event.get():
        if event.type == QUIT or quitButton.handleEvent(event):
            pygame.quit()
            sys.exit()

        if newButton.handleEvent(event):
            game.reset()

        if hitButton.handleEvent(event):
            game.hit()

        if stayButton.handleEvent(event):
            game.stay()

    background.draw()
    game.draw()
    hitButton.draw()
    stayButton.draw()
    newButton.draw()
    quitButton.draw()

    pygame.display.update()
    clock.tick(30)

        