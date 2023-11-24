import random

def generate_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    return deck
    
def shuffle_deck(deck):
    random.shuffle(deck)
    
def deal_cards(deck, num_players=4):
    hands = [[] for _ in range(num_players)]
    for i in range(len(deck)):
        player_index = i % num_players
        hands[player_index].append(deck[i])
    return hands
    
def display_hands(hands):
    for i, hand in enumerate(hands):
        print('Player {}: {}'.format(i+1, ', '.join(['{} of {}'.format(card['rank'], card['suit']) for card in hand])))
        
def run():
    deck = generate_deck()
    shuffle_deck(deck)
    print(len(deck))
    hands = deal_cards(deck)
    display_hands(hands)
    
if __name__ == '__main__':
    run()