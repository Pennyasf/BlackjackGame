import random

#function to add another card (currently the player chooses at random)
def extra_card(players, deck_of_cards):
    value = -1
    for i in players:
        value += 1
        extra_card = random.choice([True, False])
        if extra_card == True:
            print("player", value, "has chosen to hit")
            current_cards = players[list(players)[value]]
            card_chosen = random.choice(deck_of_cards)
            deck_of_cards.remove(card_chosen)
            current_cards.append(card_chosen)
        else:
            print("player", value, "has chosen to stand")
    return(players, deck_of_cards)


#function to check the current score of each players hand
def check_score(players):
    value = -1
    for i in players:
        value += 1
        temp_double = players[list(players)[value]]
        total = 0

        for each in temp_double:
            temp_val = temp_double[0]
            if (temp_val == "Jack" or temp_val == "Queen" or temp_val == "King"):
                temp_val = 10
            elif temp_val == "Ace":
                temp_val = 1
            else:
                temp_val = temp_val
            total = total + temp_val
        

        #checking for any winners or busts
        if total == 21: 
            players[list(players)[value]] = "winner"
            print("winner")
            print(players[list(players)[value]])
            return(players, True)
        elif total == 11:
            if (temp_val_1 == 1 or temp_val_2 == 1):
                players[list(players)[value]] = "winner"
                print("winner")
                print(players[list(players)[value]])
                return(players, True)
        elif total > 21:
            print(players[list(players)[value]])
            print("bust")
            players[list(players)[value]] = "bust"
    return(players, False)
    

#function to assign each player their total and order them based on this number, and then display this as a 'leaderboard'
def final_leaderboard(players):
    value = -1
    for i in players:
        value += 1
        temp_tuple = players[list(players)[value]]
        print(temp_tuple)
        total = 0

        for each in temp_tuple:
            temp_val = temp_tuple[0]
            if (temp_val == "Jack" or temp_val == "Queen" or temp_val == "King"):
                temp_val = 10
            elif temp_val == "Ace":
                temp_val = 1
            else:
                temp_val = int(temp_val)
            total = total + temp_val

        players[list(players)[value]] = total
        
        if players[list(players)[value]] == "bust":
            players[list(players)[value]] = 0
        elif players[list(players)[value]] == "winner":
            players[list(players)[value]] = 21

    sorted(players, key=players.get)
    return(players)


def main():
    #setting up players and deck
    num_of_players = input('How many players are playing?')
    deck_of_cards = ["Ace","Ace","Ace","Ace",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,"Jack","Jack","Jack","Jack","Queen","Queen","Queen","Queen","King","King","King","King"]
    players = {}
    num_of_players = int(num_of_players)

    #Giving out initial cards for the players
    for i in range (0,num_of_players):
        players["player{0}".format(i+1)] = []
        card1 = random.choice(deck_of_cards)
        deck_of_cards.remove(card1)
        card2 = random.choice(deck_of_cards)
        deck_of_cards.remove(card2)
        cards = [card1, card2]
        players[list(players)[i]] = cards
        

    #using check_score() to look for any winners already
    (players, winner) = check_score(players)
    if winner == True:
        print("finished")

        final_leaderboard(players)
        print(players)

        exit()

    #calling the extra card function 
    extra_card(players, deck_of_cards)
    print(players)

    #again checking for winners and busts
    (players, winner) = check_score(players)
    if winner == True:
        print("finished")

        final_leaderboard(players)
        print(players)

        exit()

    #if no winners have already been established, a final leaderboard is produced
    final_leaderboard(players)
    
    pass

main()