# Filip Hjerten's Bubble Click Game, Please read README before giving it a try!

import pygame
import pygwidgets
import random
import sys

class Bubble:
    def __init__(self, windowWidth, windowHeight):
        self.windowWidth = windowWidth  
        self.windowHeight = windowHeight 

        self.size = random.randint(20, 50)     # random bubble size
        self.speed = random.uniform(3, 6)      # random speed of bubble

        self.reset() 

    def move(self):
        self.y -= self.speed   # moving the bubble/s upward

        # if bubble goes off screen it gets reseted.
        if self.y < 0:
            self.reset()

    def reset(self):
        # places bubble at new random positon at bottom
        self.x = random.randint(0, self.windowWidth)
        self.y = random.randint(self.windowHeight, self.windowHeight + 100)

    def draw(self, window):
        pygame.draw.circle(window, (100, 150, 255),
                           (int(self.x), int(self.y)), self.size)

    def isClicked(self, mousePos):
        mx, my = mousePos  # mouse x and y position

        # distance formula to check how close click is to bubble center. (Learned in my CSC391 class)
        distance = ((self.x - mx) ** 2 + (self.y - my) ** 2) ** 0.5

        return distance < self.size  # if inside bubble = true

pygame.init()

windowWidth = 800
windowHeight = 600
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Bubble Click Game")

clock = pygame.time.Clock()  # controls the game speed in frames / second

# font for game over text
font = pygame.font.SysFont(None, 60)  # create font witg size 60.


# ---------- UI ----------
startButton = pygwidgets.TextButton(window, (350, 500), 'Start')  # clickable button
scoreText = pygwidgets.DisplayText(window, (20, 20), 'Score: 0')  # shows score
timerText = pygwidgets.DisplayText(window, (650, 20), 'Time: 30') # shows time


bubbles = []
for _ in range(8):  # creates 8 bubbles
    bubbles.append(Bubble(windowWidth, windowHeight))

score = 0
timeleft = 30
gameStarted = False  # game starts when button clicked only.

while True:
    clock.tick(30)  # run game at 30 frames per second

    # ---- Events ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if startButton.handleEvent(event):  # check if button is clicked
            gameStarted = True
            score = 0
            timeleft = 30

        if event.type == pygame.MOUSEBUTTONDOWN and gameStarted:
            for bubble in bubbles:
                if bubble.isClicked(pygame.mouse.get_pos()):
                    score += 1
                    bubble.reset()  # remove bubble after click and create new.

    if gameStarted:
        timeleft -= 1 / 30  # decrease time every frame

        for bubble in bubbles:
            bubble.move() 

        if timeleft <= 0:
            gameStarted = False  # when time is out, game stops.


    # drwaing it all.
    window.fill((255, 255, 255))

    for bubble in bubbles:
        bubble.draw(window)

    scoreText.setValue(f"Score: {score}")
    timerText.setValue(f"Time: {int(timeleft)}")

    scoreText.draw()
    timerText.draw()
    startButton.draw()

    # the Game over text.
    if not gameStarted and timeleft <= 0:
        # create text image
        gameOverText = font.render(f"Game Over! Score: {score}", True, (0, 0, 0))

        # center the text on screen
        textRect = gameOverText.get_rect(center=(windowWidth // 2, windowHeight // 2))

        window.blit(gameOverText, textRect)  # draw text on screen

    pygame.display.update()