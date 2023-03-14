from cards import PlayingCards

#Initilalize game setting
number_of_decks = 2
number_of_games = 1000

money = 1000
bet = 10
won = 0
lost = 0

#Initialize the playing cards
cards = PlayingCards(number_of_decks)
cards.shuffle()


#Deal the initial cards
def initial_deal(player_cards, dealer_cards):
    player_cards.append(cards.draw())
    dealer_cards.append(cards.draw())
    player_cards.append(cards.draw())
    dealer_cards.append(cards.draw())

    return player_cards, dealer_cards

#Checks if the hand is a Black Jack
def check_black_jack(cards):
    black_jack = False
    if (cards[0].max_value + cards[1].max_value) == 21:
        black_jack = True

    return black_jack


def game():
    global money, won, lost
    player_cards = []
    dealer_cards = []

    player_cards, dealer_cards = initial_deal(player_cards, dealer_cards)

    print(f"Player cards: {player_cards[0]} {player_cards[1]}")
    print(f"Dealer cards: {dealer_cards[0]} {dealer_cards[1]}")

    if check_black_jack(player_cards):
        #Player has BJ
        if check_black_jack(dealer_cards):
            print("Both player and dealer have BJs")
        else:
            print("Player wins by having a BJ")
            money += bet * 3 / 2
            won += 1
    else:
        #No BJ for the player
        if check_black_jack(dealer_cards):
            print("Dealer wins by having a BJ")
            money -= bet
            lost += 1
        
    

for _ in range(0, number_of_games):
    if cards.cards_remaining() / cards.total_number_of_cards() < 0.25:
        cards.shuffle()
    game()

print(f"Final money: {money}")
print(f"Games won: {won}")
print(f"Games lost: {lost}")

    
