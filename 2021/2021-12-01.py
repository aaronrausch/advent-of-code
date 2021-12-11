
with open('inputs/2021-12-01.txt') as f:
    depths = [int(d) for d in f.read().splitlines()]

part_1 = sum(p < v for p, v in zip(depths, depths[1:]))
print(part_1)

part_2 = sum(p < v for p, v in zip(depths, depths[3:]))
print(part_2)