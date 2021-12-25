
with open('inputs/2021-12-25.txt') as f:
    sea = [[l for l in row] for row in f.read().splitlines()]
    HEIGHT, WIDTH = len(sea), len(sea[0])

def search(sea, char):
    coords = []
    for i, row in enumerate(sea):
        for j, item in enumerate(row):
            if item == char:
                coords.append( (i, j) )
    return coords

def update(updates):
    for coord, update in updates.items():
        i, j = coord
        sea[i][j] = update

def move_right(char):
    updates = {}
    for coord in search(sea, char):
        i, j = coord
        nxt = (j + 1) % WIDTH
        if sea[i][nxt] == '.':
            updates[ (i, nxt) ] = char
            updates[ (i, j) ] = '.'
            global change; change = True
    update(updates)

def move_down(char):
    updates = {}
    for coord in search(sea, char):
        i, j = coord
        nxt = (i + 1) % HEIGHT
        if sea[nxt][j] == '.':
            updates[ (nxt, j) ] = char
            updates[ (i, j) ] = '.'
            global change; change = True
    update(updates)

iterations = 0
change = True
while change:

    iterations += 1
    change = False
    move_right('>')
    move_down('v')

print(iterations)