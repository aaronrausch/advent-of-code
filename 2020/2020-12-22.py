

with open('inputs/2020-12-22.txt') as deck_data:
    deck = [line[:-1] for line in deck_data]
    player_one = [int(card) for card in deck[1:26]]
    player_two = [int(card) for card in deck[28:54]]
