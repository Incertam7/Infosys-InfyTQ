#DSA-Tryout
import random

card_suits = ['C', 'D', 'H', 'S']
card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def generate_cards_per_type(card_type):
    suit_cards = []
    for rank in card_ranks:
        suit_cards.append(card_type + rank)
        
    return suit_cards

def generate_card_deck():
    deck_of_cards = []
    for suit in card_suits:
        cards_per_suit = generate_cards_per_type(suit)
        for card in cards_per_suit:
            deck_of_cards.append(card)
    return deck_of_cards

def shuffle_card_deck(cards_list):
    for i in range(0, 52):
        index1 = random.randrange(0, 26)
        index2 = random.randrange(26, 52)
        swap(cards_list, index1, index2)
    return cards_list
        
def swap(cards_list, index1, index2):
    temp = cards_list[index1]
    cards_list[index1] = cards_list[index2]
    cards_list[index2] = temp

def sort_cards_of_each_player(cards_list):
    for i in range(0, 12):
        swapped = False
        for j in range(0, 12 - i):
            suit1 = card_suits.index(cards_list[j][0])
            suit2 = card_suits.index(cards_list[j + 1][0])
            if suit1 > suit2:
                swap(cards_list, j, j + 1)
                swapped = True
            elif suit1 == suit2:
                rank1 = card_ranks.index(cards_list[j][1:])
                rank2 = card_ranks.index(cards_list[j + 1][1:])
                if rank1 > rank2:
                    swap(cards_list, j, j + 1)
                    swapped = True
        if not swapped:
            break
    return cards_list  

def allocate_cards_to_players(cards_list):
    i = 0
    player1_cards = []
    player2_cards = []
    player3_cards = []
    player4_cards = []

    while(i < 52):
        player1_cards.append(cards_list[i])
        i += 1
        player2_cards.append(cards_list[i])
        i += 1
        player3_cards.append(cards_list[i])
        i += 1
        player4_cards.append(cards_list[i])
        i += 1
    
    player_cards_dict = {}
    player_cards_dict["Player1"] = player1_cards
    player_cards_dict["Player2"] = player2_cards
    player_cards_dict["Player3"] = player3_cards
    player_cards_dict["Player4"] = player4_cards
    
    return player_cards_dict

def prepare_cards():
    cards_list = generate_card_deck()
    print("Generated cards:\n", cards_list, "\n")
    cards_list = shuffle_card_deck(cards_list)
    print("Shuffled cards:\n", cards_list, "\n")
    player_hands = allocate_cards_to_players(cards_list)
    start_player = None
    print("The cards have been dealt")
    for key in sorted(player_hands.keys()):
        player_hands[key] = sort_cards_of_each_player(player_hands[key])
        print(key, ":", player_hands[key], "\n")
        if 'CA' in player_hands[key]:
            start_player = key
    return start_player

first_player = prepare_cards()
print("The first player is:", first_player)
