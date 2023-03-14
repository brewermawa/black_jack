import random

faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["♠", "♣", "♢", "♡"]

class Card:
    def __init__(self, face, suit, min_value, max_value):
        self.face = face
        self.suit = suit
        self.min_value = min_value
        self.max_value = max_value

    def __str__(self):
        return f"{self.face} {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for face in faces:
                if face in ["J", "Q", "K", "A"]:
                    min__value = 1 if face == "A" else 10
                    max_value = 11 if face == "A" else 10
                else:
                    min_value = max_value = int(face)
                
                card = Card(face, suit, min_value, max_value)
                self.cards.append(card)

class PlayingCards:
    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.cards = []
        deck = Deck()

        for _ in range(0, number_of_decks):
            for card in deck.cards:
                self.cards.append(card)

    def total_number_of_cards(self):
        return self.number_of_decks * 52
    
    def cards_remaining(self):
        return len(self.cards)
    
    def shuffle(self):
        self.__init__(self.number_of_decks)
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)