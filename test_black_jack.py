#testing against an invalid card value
test_invalid_card_value_number:
    players = {player1: 2,3 player2: 20,1}
    deck_of_cards = ["Ace","Ace","Ace","Ace",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,"Jack","Jack","Jack","Jack","Queen","Queen","Queen","Queen","King","King","King","King"]
    extra_card(players,deck_of_cards)
    raise ValueError("Should not accept a card having a value above 11")

test_invalid_card_value_word:
    players = {player1: 2,3 player2: "bob",1}
    deck_of_cards = ["Ace","Ace","Ace","Ace",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,"Jack","Jack","Jack","Jack","Queen","Queen","Queen","Queen","King","King","King","King"]
    extra_card(players,deck_of_cards)
    raise ValueError("Should not accept a card having a value as not a number or given words")

#testing against if there are not enough cards
test_not_enough_cards:
    players = {player1: 2,3 player2: 9,1}
    deck_of_cards = [1,2]
    extra_card(players,deck_of_cards)
    raise ValueError("Should not be able to deal cards when there are not enough left")

"""
More tests to think about:
-User inputs a number of players that is far too high

"""