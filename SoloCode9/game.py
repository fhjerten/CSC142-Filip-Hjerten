import pygwidgets
from constants import *
from Deck import *

class Game:

    def __init__(self, window):
        self.window = window
        self.deck = Deck(window)

        # text in middle
        self.message = pygwidgets.DisplayText(
            window, (50, 250), "",width=900, justified='center',fontSize=36, textColor=WHITE)

        self.reset()

    def reset(self):
        self.deck.shuffle()
        self.player = []
        self.dealer = []

        # deal 2  cards each side
        for i in range(2): #loop runs twice.
            self.player.append(self.deck.getCard())
            self.dealer.append(self.deck.getCard())

        # player cards (bottom)
        for i, card in enumerate(self.player): # i = position
            card.setLoc((200 + i * 120, 400))  # set loc moves the card to x or y on screen. in this case right.
            card.reveal()

        # dealer cards (top)
        for i, card in enumerate(self.dealer):
            card.setLoc((200 + i * 120, 100))
            if i == 0:
                card.reveal()   # show first
            else:
                card.conceal() # hide second


        self.message.setValue("Hit or Stay")

    def calculate_score(self, hand):
        score = 0
        has_ace = False

        for card in hand:
            rank = card.getRank()

            try:
                score += int(rank)   # number cards (2-10)
            except:
                if rank == 'Ace':
                    has_ace = True # handes aces later
                else:
                    score += 10      # face cards are worth 10.

        # ace is 1 or 11
        if has_ace:
            if score + 11 > 21:
                score += 1
            else:
                score += 11

        return score

    def hit(self):
        card = self.deck.getCard()
        card.setLoc((200 + len(self.player) * 120, 400)) # place next to exsiting cards in position.
        card.reveal()
        self.player.append(card)

        # check bust
        if self.calculate_score(self.player) > 21:
            self.message.setValue("You busted! Dealer wins.")

    def stay(self):
        # show dealer cards
        for card in self.dealer:
            card.reveal()

        # dealer goes on until 17
        while self.calculate_score(self.dealer) < 17:
            card = self.deck.getCard()

            # for new dealer card.
            card.setLoc((200 + len(self.dealer) * 120, 100))
            card.reveal()
            self.dealer.append(card)

        player_score = self.calculate_score(self.player)
        dealer_score = self.calculate_score(self.dealer)

        # decide winner
        if dealer_score > 21:
            self.message.setValue("Dealer busted! You win.")
        elif dealer_score > player_score:
            self.message.setValue("Dealer wins.")
        elif dealer_score < player_score:
            self.message.setValue("You win!")
        else:
            self.message.setValue("Tie.")

    def draw(self):
        for card in self.player: # draw players cards
            card.draw()
        for card in self.dealer: # draw dealers cards
            card.draw()

        #drawing text
        self.message.draw()