
with open('inputs/2021-12-01.txt') as f:
    depths = [int(d) for d in f.read().splitlines()]


# PART 1
c = 0

for i, d in enumerate(depths):

    if i < 1:
        continue

    if d > depths[i - 1]:
        c += 1

print(c)


# PART 2
c = 0

for i, d in enumerate(depths):

    if i < 3:
        continue

    try:
        w = d + depths[i + 1] + depths[i + 2]
        pw = depths[i - 1] + d + depths[i + 1]
        if w > pw:
            c += 1
    except IndexError:
        pass

print(c)
