A Python practice project

The objective of the project is to put into action all the tutorials, books, etc. about Python that I've completed in the previous year.

The project will be to code an app that can give you complete stats of the card game Black Jack.

The final version will be a web based app using the Django web framework where the user will be able to select different options and then simulate a finite number of plays to obtain the statistics of the session.

It will be built in sections:

.....

Cards module
Description: Python module where the playing cards settings are initialized
Used by: Blackjack module
Uses modules: The card module will not need to access any other module

Classes
    Card: Holds the properties of each card
    Properties:
        face: the face of the card (2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A)
        suit: the suit of the card (hearts, clubs, diamonds, spades)
        min_value: in all the number cards the face is the min_value. The J, Q, K have a value of 10, A has a min_value of 1
        max_value: in all the number cards the face is the min_value. The J, Q, K have a value of 10, A has a max_value of 11

    Methods:
        __init__: Receives the value of the four porperties as parameters, sets the 4 properties
        __str__: Returns the face and the suit as a joines string


    Deck:
    Properties:
        cards = A list to hold the card objects

    Methods:
        __init__: Receives no parameters, creates the full deck of 52 cards


    PlayingCards: Holds all the playing cards available for play
    Properties:
        number_of_decks: The number of decks used for play
        cards = A list to hols all the cards available for play

    Methods:
        __init__: Receives the number of decks as a parameter
                  Initialize the cards property to an empty list
                  Creates a deck object (using the Deck class)
                  Loop the deck object the amount of times dictaded by the number_of_decks property and append each card to the cards property

        total_number_of_cards: Returs number_of_decks * 52

        cards_remaining: Returns the cards remaining

        shuffle: Call the __init__ method to initialize the playing cards
                 Shuffle the list using the random.shuffle function

        draw: Remove and return the first card in the list (using the pop function at position 0)

Blackjack module
Description: This module will have all the logic that handles the blackjack actions
Used by: The main module will be the only one to directly access the blackjack module
Uses modules: The blackjack module will access the card an strategy modules

Steps in a black jack round:
1.- Initial deal (2 cards each player and dealer)
2.- Check for black jack
3.- Player turn (needs the 2 player cards and the first dealer card, uses the strategy module)
4.- Dealer turn (needs the 2 dealer cards, uses basic black jack rules to decide cards to draw)
5.- Calculate result
6.- Shuffle the deck if less than 25% is left

Classes
    Blackjack: Holds the properties and methods necessary to control the playng cards and to deal with the player and dealer hands using the strategy module
    Properties:
        shoe: A list containing the playing cards
        player_cards: list containing the player cards
        dealer_cards: list containing the dealer cards

    Methods:
        __init__: Receives the number of decks as a parameter
                  Initializes the playing cards using the Card module

        deal: Uses the playing_cards method to deal 2 cards each alternating between player and dealer

        check_blackjack: If the player has black jack
                             If the dealer has blackjack
                                 Declare a tie
                                 Finish the round
                             else
                                 Declare the player as winner
                                 Finish the round
                         else (the player does not have blackjack)
                             If the dealer has blackjack
                                 Declere the dealer as winner
                             else (neither the player nor the dealer have backjacks)
                                 Exit the method to continue to the next step
                            
        
        player_turn: Uses the 2 player cards and the first dealer card to decide the next step. 
                     Possible combinations:
                        1.- Hard total (2 different cards that are not A)
                        2.- Soft total (an A and another card)
                        3.- Pair (2 cards with the same face)
                     Depending on the strategy (uses the strategy module) the possible outcomes are
                        1.- Stand
                        2.- Hit
                        3.- Double
                        4.- Split


Strategy module


Main module



