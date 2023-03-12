from cards import PlayingCards

playingCards = PlayingCards(2)

print(f"Number of decks: {playingCards.numberOfDecks}")
print(f"Total number of cards: {playingCards.totalNumberOfCards()}")

playingCards.shuffle()

print(playingCards.draw())
print(f"Cards reemaining: {playingCards.cardsRemaining()}")
print(playingCards.draw())
print(f"Cards reemaining: {playingCards.cardsRemaining()}")
print(playingCards.draw())
print(f"Cards reemaining: {playingCards.cardsRemaining()}")
print(playingCards.draw())
print(f"Cards reemaining: {playingCards.cardsRemaining()}")
print(playingCards.draw())
print(f"Cards reemaining: {playingCards.cardsRemaining()}")