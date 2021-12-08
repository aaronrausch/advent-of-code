
with open('inputs/2021-12-02.txt') as input_file:
    course = [nav for nav in input_file.read().splitlines()]


# PART 1
pos, depth = 0, 0

for ins in course:

    nav, am = ins.split()
    am = int(am)

    if nav == 'forward':
        pos += am
    elif nav == 'up':
        depth -= am
    elif nav == 'down':
        depth += am

print(pos * depth)


# PART 2
pos, depth, aim = 0, 0, 0

for ins in course:

    nav, am = ins.split()
    am = int(am)

    if nav == 'down':
        aim += am
    elif nav == 'up':
        aim -= am
    elif nav == 'forward':
        pos += am
        depth += aim * am

print(pos * depth)
