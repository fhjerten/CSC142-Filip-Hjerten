import pygame
import pygwidgets

class Card():

    BACK_OF_CARD_IMAGE = pygame.image.load('images/BackOfCard.png')

    def __init__(self, window, rank, suit, value):
        self.window = window
        self.rank = rank
        self.suit = suit
        self.value = value

        # name like "ace of spades"
        self.cardName = rank + " of " + suit

        fileName = 'images/' + self.cardName + '.png'

        # store front and back images
        self.images = pygwidgets.ImageCollection(
            window, (0, 0),
            {'front': fileName, 'back': Card.BACK_OF_CARD_IMAGE},
            'back'
        )

    def conceal(self):
        self.images.replace('back')  # hide card

    def reveal(self):
        self.images.replace('front')  # show card

    def getValue(self):
        return self.value

    def getRank(self):
        return self.rank

    def setLoc(self, loc):
        self.images.setLoc(loc)  # move card to x y

    def draw(self):
        self.images.draw()  # draw card on screen.