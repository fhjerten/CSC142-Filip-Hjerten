import pygame
import sys
import random

class Raindrop:
    __slots__ =["x", "y", "radius"] #only allowed variables
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1  # starting small

    def update (self):
        self.radius += 1  # radius grows over time.

    def draw(self, window):
        pygame.draw.circle(window, (0, 0, 255), (self.x, self.y), self.radius) # blue colored raindrop


class RaindropManager:
    RAIN_RATE = 500  # milliseconds between each raindrop
    MAX_RADIUS = 50

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        self.raindrops = [] # list of raindrops
        self.last_time = 0 # last time a raindrop was made.

    def run(self):
        while True: # main game loop

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            #creating new raindrop baased on time
            current_time = pygame.time.get_ticks()
            if current_time - self.last_time > self.RAIN_RATE:
                self.last_time = current_time # reset timer

                x = random.randint(0, 800) # new x position.
                y = random.randint(0, 600) # new y position.

                new_drop = Raindrop(x, y) # create new raindrop
                self.raindrops.append(new_drop) # add new to list

            #removing too big drops
            self.raindrops = [d for d in self.raindrops if d.radius < self.MAX_RADIUS] # "d" each raindrop in list.

            #updating everything
            for d in self.raindrops:
                d.update()

            #drawing the game
            self.window.fill((255, 255, 255)) # white background
            for d in self.raindrops:
                d.draw(self.window)
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    manager = RaindropManager()
    manager.run()