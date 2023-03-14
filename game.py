from blackjack import Blackjack, Result

number_of_decks = 6
number_of_hands = 10

money = 1000
bet = 10
player_blackjacks = 0
dealer_blackjacks = 0
won = 0
lost = 0
tie = 0

game = Blackjack(number_of_decks)

result = Result()

for _ in range(1, number_of_hands):
    result = game.deal()
    money += result.bet * bet
    player_blackjacks += result.player_blackjack
    dealer_blackjacks += result.dealer_blackjack
    won += 1 if result.winner == "P" else 0
    lost += 1 if result.winner == "D" else 0
    tie += 1 if result.winner == "T" else 0

print(f"Money: {money}")
print(f"Player Blackjacks: {player_blackjacks}")
print(f"Dealer Blackjacks: {dealer_blackjacks}")
print(f"Won: {won}")
print(f"Lost: {lost}")
print(f"Ties: {tie}")

