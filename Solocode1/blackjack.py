import random

def draw_card(hand, deck):
    hand.append(deck.pop())  # take last card from deck.




def calculate_hand(hand): # Section for calculating hand values in blackjack.
    total = 0
    aces = 0

    for card in hand: # looks at one card at a time.

        if card in ["J", "Q", "K"]:  # for face cards, value is 10.
            total += 10

        # First case for aces, can either be 1 or 11, which will come later.
        elif card == "A":
            aces += 1
        else:
            total += int(card) # For regular number cards.

    total += aces

        # If you get an ace and the total score doesn't go over 21 the ace counts as an 11.
    if aces > 0 and total + 10 <= 21:
        total += 10
   
    return total # sends the total value of the hand back when score is calculated.




def main():
    # Shared (one) deck of cards for both player and dealer hand. Only one deck used for this.
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    player_hand = []
    dealer_hand = []

    # shuffle the deck.
    random.shuffle(deck)
    
    # Logic of the game, dealer starts with getting one card, then player recieves two cards.
    draw_card(dealer_hand, deck)
    draw_card(player_hand, deck)
    draw_card(player_hand, deck)


    print ("Dealer's hand:", dealer_hand[0]) # Only showing one card of dealer as second is hidden.
    print ("Dealer's score:", calculate_hand(dealer_hand[:1])) # Showing score of dealer's visible card only.
    print ("Player's hand:", player_hand)
    print ("Your score", calculate_hand(player_hand))


    # Time for the player to make choices.
    while True:
        choice = input("Do you want to hit or stay? h for hit s for stay(h/s): ")
        if choice == 'h':
            draw_card(player_hand, deck)
            print ("Total score:", calculate_hand(player_hand))

            if calculate_hand(player_hand) > 21:
                print("You busted! Dealer wins.")
                return
             
        elif choice == 's':
            break

    # Dealer's turn, has to stay on 17, hit if less than 17.
    while calculate_hand(dealer_hand) < 17:
        draw_card(dealer_hand, deck)

        print("Dealer's score:", calculate_hand(dealer_hand))

        while calculate_hand(dealer_hand) == 17:
            break

        # Dealer loss if going over 21.
        if calculate_hand(dealer_hand) > 21:
            print("Dealer busted! You win.")
            return
        

    
    print("Dealer's total score:", calculate_hand(dealer_hand))
    print("Player's score:", calculate_hand(player_hand))

    # Determining winner.
    if calculate_hand(player_hand) > calculate_hand(dealer_hand):
        print("You win!")
    elif calculate_hand(player_hand) < calculate_hand(dealer_hand):
        print("Dealer wins!")
    else:
        print("It's a push, no one wins")
        



if __name__ == "__main__":
    main()