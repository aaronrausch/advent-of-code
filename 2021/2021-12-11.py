
with open('inputs/2021-12-11.txt') as f:
    octopi = [[int(n) for n in l] for l in f.read().splitlines()]

def inbounds(i, j):
    row_inbounds = 0 <= i < len(octopi)
    col_inbounds = 0 <= j < len(octopi[0])
    return (row_inbounds and col_inbounds)

def increment(octopi):
    for i, row in enumerate(octopi):
        for j, oc in enumerate(row):
            octopi[i][j] += 1

def simultaneous(octopi):
    simul = True
    for row in octopi:
        for oc in row:
            if oc != 0:
                simul = False
    return simul

def flash(octopi, i, j, done):
    cycle_flashes = 0
    nearby = [
        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
        (i, j - 1), (i, j + 1),
        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
    ]
    current = octopi[i][j]

    if current > 9 and current not in done:

        cycle_flashes += 1
        done.add( (i, j) ) # this octopus cannot flash again
        octopi[i][j] = 0

        for i, j in nearby:
            if inbounds(i, j) and (octopi[i][j] != 0): #s check that octopus did not flash on the same cycle
                octopi[i][j] += 1
                cycle_flashes += flash(octopi, i, j, done)

    return cycle_flashes

cycle, flashes = 0, 0
done = set()
searching = True
while searching:

    cycle += 1
    increment(octopi)

    for i, row in enumerate(octopi):
        for j, oc in enumerate(row):
            flashes += flash(octopi, i, j, done)

    if cycle == 100:
        print(f'CYCLE {cycle} : {flashes}')

    if simultaneous(octopi):
        print(f'SIMULTANEOUS FLASH : {cycle}')
        searching = False
