
from itertools import combinations
from math import prod

with open('inputs/2020-12-01.txt') as raw_data:
    years = [int(year) for year in raw_data.read().splitlines()]

for year in years:
    if (2020 - year) in years:
        print(year * (2020 - year))

three_sum = [c for c in combinations(years, 3)]
for sum_ in three_sum:
    if sum(sum_) == 2020:
        print(prod(sum_))
