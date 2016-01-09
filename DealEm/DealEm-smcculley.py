players_number = int(float(input("How many players are there?")))
while(players_number < 1):
    players_number = int(input("How many players are there?"))

cards_in_hand = int(float(input("How many cards are there in each hand?")))
while(cards_in_hand < 1):
    cards_in_hand = int(input("How many cards are there in each hand?"))


card_values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suits = ("c", "h", "s", "d")

import random

for i in range(players_number):
    print("\nPlayer", str(i + 1) + "'s hand contains:")
    for j in range(cards_in_hand):
        random_card = random.randrange(len(card_values))
        random_suit = random.randrange(len(suits))
        print(card_values[random_card] + suits[random_suit], end=" ")
    print("\n")

