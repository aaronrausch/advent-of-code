
with open('inputs/2020-12-03.txt') as data:
    landmap = [row for row in data.read().splitlines()]


def traverse(x_speed, y_speed, landscape):

    landscape_size = len(landmap[0])  # Check size before tiling
    trees = 0
    position = 0

    for y in range(0, len(landscape), y_speed):
        if landscape[y][position] == '#':
            trees += 1
        position += x_speed
        position %= landscape_size
    return trees


# PART 1
print(traverse(3, 1, landmap))

# PART 2
print(traverse(1, 1, landmap) * traverse(3, 1, landmap) * traverse(5,
                                                                   1, landmap) * traverse(7, 1, landmap) * traverse(1, 2, landmap))
