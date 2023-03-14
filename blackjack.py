from cards import PlayingCards

class Result:
    def __init__(self):
        self.end = False          #Flags if the game ended
        self.winner = ""          #P if player won, D if dealer won, T if its a push
        self.bet = 0              #The number of bets won or lost (1 for a normal win, 1.5 for a BJ win, -1 if bet lost. Could be higher in case of splits or doubles)
        self.player_blackjack = 0 #Number of blackjack the player got (could be more than 1 if it was a split game)
        self.dealer_blackjack = 0 #The dealer can only have either 0 or 1 blackjack

    def __str__(self):
        return f"Game ended: {self.end}, Winner: {self.winner}, Bet: {self.bet}, P BJ: {self.player_blackjack}, D BJ: {self.dealer_blackjack}"


class Blackjack:
    def __init__(self, number_of_decks):
        self.shoe = PlayingCards(number_of_decks)
        self.shoe.shuffle()
        self.player = []
        self.dealer = []

    def deal(self):
        self.result = Result()
        self.player = []
        self.dealer = []
        self.player.append(self.shoe.draw())
        self.dealer.append(self.shoe.draw())
        self.player.append(self.shoe.draw())
        self.dealer.append(self.shoe.draw())

        #print(self.player[0], self.player[1])
        #print(self.dealer[0], self.dealer[1])

        self.result = self.check_blackjack()
        return self.result

    def check_blackjack(self):
        #REMOVE
        if (self.shoe.cards_remaining() / self.shoe.total_number_of_cards()) < 0.25:
            self.shoe.shuffle()
        #REMOVE

        player_1 = self.player[0]
        player_2 = self.player[1]
        dealer_1 = self.dealer[0]
        dealer_2 = self.dealer[1]

        player_black_jack = (player_1.max_value + player_2.max_value) == 21
        dealer_black_jack = (dealer_1.max_value + dealer_2.max_value) == 21

        if player_black_jack and dealer_black_jack:
            self.result.end = True
            self.result.winner = "T"
            self.result.bet = 0
            self.result.player_blackjack = 1
            self.result.dealer_blackjack = 1
            return self.result

        if player_black_jack and not dealer_black_jack:
            self.result.end = True
            self.result.winner = "P"
            self.result.bet = 1.5
            self.result.player_blackjack = 1
            self.result.dealer_blackjack = 0
            return self.result

        if not player_black_jack and dealer_black_jack:
            self.result.end = True
            self.result.winner = "D"
            self.result.bet = -1
            self.result.player_blackjack = 0
            self.result.dealer_blackjack = 1
            return self.result

        if not player_black_jack and not dealer_black_jack:
            self.result.end = False
            return self.result #Instead of returning, go to the next step

        