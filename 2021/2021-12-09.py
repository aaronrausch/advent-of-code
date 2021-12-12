
with open('inputs/2021-12-09.txt') as file:
    cave = [l for l in file.read().splitlines()]
    cave = [[int(el) for el in row] for row in cave]

def find_neighbors(r, c):
    return [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]

def inbounds(r, c):
    row_inbounds = r >= 0 and r < len(cave)
    column_inbounds = c >= 0 and c < len(cave[0])
    if not (row_inbounds and column_inbounds):
        return False
    return True

def checks(r, c, visited):
    if not inbounds(r, c): return False
    if cave[r][c] == 9: return False
    if (r, c) in visited: return False
    return True

def find_lows(cave):
    low_points = []
    for r, _ in enumerate(cave):
        for c, _ in enumerate(cave[0]):
            lowest = True
            for rc, cc in find_neighbors(r, c):
                if inbounds(rc, cc) and (cave[r][c] >= cave[rc][cc]):
                    lowest = False
            if lowest: low_points.append(cave[r][c])
    return low_points

def basin_sizes(cave):
    visited = set()
    sizes = []
    for r, _ in enumerate(cave):
        for c, _ in enumerate(cave[0]):
            size = explore_size(cave, r, c, visited)
            if size: sizes.append(size)
    return sizes

def explore_size(cave, r, c, visited):
    size = 0
    stack = [ (r, c) ]
    while stack:
        current = stack.pop()
        r, c = current
        if checks(r, c, visited):

            visited.add(current)
            size += 1

            neighbors = find_neighbors(r, c)
            for coord in neighbors:
                r, c = coord
                if checks(r, c, visited):
                    stack.append((r, c))

    return size

# PART 1
risk_levels = 0
for point in find_lows(cave):
    risk_levels += point + 1
print(f'PART ONE : {risk_levels}')

# PART 2
sizes = basin_sizes(cave)
sizes = sorted(sizes)
print(f'PART TWO : {sizes[-3] * sizes[-2] * sizes[-1]}')
