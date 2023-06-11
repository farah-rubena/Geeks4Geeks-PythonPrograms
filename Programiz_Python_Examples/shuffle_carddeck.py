'''WAPP to shuffle a deck of cards'''

import random

def shuffle_cards():

    ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    deck = [(rank, suit) for rank in ranks for suit in suits]

    random.shuffle(deck)

    for card in deck:
        return f"You've got {card[0]} of {card[1]}"

res = shuffle_cards()
print(res)