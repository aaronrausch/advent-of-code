
with open('inputs/2021-12-04.txt') as input_file:

    f = [r for r in input_file.read().splitlines()]
    random_numbers = [int(r) for r in f[0].split(',') if r.isdigit()]

    boards_start = 2
    board_size = 5
    bingo_cards = [f[c:c + board_size]
                   for c in range(boards_start, len(f), board_size + 1)]
    for card in bingo_cards:
        for index, row in enumerate(card):
            card[index] = [int(d) for d in row.split(' ') if d.isdigit()]


def bingo(card):
    for row in card:
        if all(r == -1 for r in row):
            return True
    for column in zip(*card):
        if all(c == -1 for c in column):
            return True
    return False


def score(card, draw):
    bingo_sum = 0
    for row in card:
        for number in row:
            if number != -1:
                bingo_sum += number
    bingo_sum *= draw
    return bingo_sum


def fill(card, draw):
    for ri, row in enumerate(card):
        for ci, number in enumerate(row):
            if number == draw:
                card[ri][ci] = -1  # using -1 as mark
    return None


order = []
for draw in random_numbers:
    for index, card in enumerate(bingo_cards):
        bingos = [t[0] for t in order]
        if index not in bingos:
            fill(card, draw)
            if bingo(card):
                order.append((index, score(card, draw)))

print(f'FIRST WINNING CARD : {order[0]}')
print(f'LAST WINNING CARD  : {order[-1]}')
