
import re

with open('inputs/2021-12-05.txt') as input_file:
    f = [r for r in input_file.read().splitlines()]
    vents = [[int(d) for d in re.findall('\d+', r)] for r in f]

size = max(max(v) for v in vents)
grid = [[0 for _ in range(size + 1)] for _ in range(size + 1)]


def count():
    count = 0
    for row in grid:
        for n in row:
            count += n > 1
    return count


def column():
    direction = 1 if y2 > y1 else -1
    for n in range(y1, y2 + direction, direction):
        grid[n][x1] += 1


def row():
    direction = 1 if x2 > x1 else -1
    for n in range(x1, x2 + direction, direction):
        grid[y1][n] += 1


def diagonal():
    x_dir = 1 if x2 > x1 else -1
    y_dir = 1 if y2 > y1 else -1
    coord = list(zip(range(x1, x2 + x_dir, x_dir),
                     range(y1, y2 + y_dir, y_dir)))
    for x, y in coord:
        grid[y][x] += 1


for vent in vents:
    x1, y1, x2, y2 = vent
    if x1 == x2:
        column()
    elif y1 == y2:
        row()
    elif x1 != x2 and y1 != y2:
        diagonal()  # for part 1, comment out
        pass

print(count())
