import random

faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["♠", "♣", "♢", "♡"]

class Card:
    def __init__(self, face, suit, low_value, high_value):
        self.face = face
        self.suit = suit
        self.low_value = low_value
        self.high_value = high_value

    def __str__(self):
        return f"{self.face} {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for face in faces:
                if face in ["J", "Q", "K", "A"]:
                    low_value = 1 if face == "A" else 10
                    high_value = 10
                else:
                    low_value = high_value = int(face)
                
                card = Card(face, suit, low_value, high_value)
                self.cards.append(card)

class PlayingCards:
    def __init__(self, numberOfDecks):
        self.numberOfDecks = numberOfDecks
        self.cards = []
        deck = Deck()

        for _ in range(0, numberOfDecks):
            for card in deck.cards:
                self.cards.append(card)

    def totalNumberOfCards(self):
        return self.numberOfDecks * 52
    
    def cardsRemaining(self):
        return len(self.cards)
    
    def shuffle(self):
        self.__init__(self.numberOfDecks)
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)