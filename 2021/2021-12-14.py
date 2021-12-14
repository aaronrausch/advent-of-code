
from parse import search, findall
from itertools import pairwise
from collections import Counter

'''This problem was very similar to the lanternfish problem, posted on 2021-12-06.
For some reason, I struggled a lot more with this problem, even though the implementation
ended up being somewhat similar. It took some hints from others for me to figure out how
to approach part 2, and especially how to extract the individual letters from the pairs.'''

with open('inputs/2021-12-14.txt') as file:
    f = file.read()
    polymer = search("{}\n", f)[0]
    FIRST, LAST = polymer[0], polymer[-1]
    ins = {r[0]: r[1] for r in findall("{:.2} -> {:.1}", f)}

pairs_counts = Counter([''.join(ll) for ll in pairwise(polymer)])
ITERATIONS = 40
for _ in range(ITERATIONS):
    addition = Counter()
    for p, c in pairs_counts.items():
        if p in ins:
            addition[p[0]+ins[p]] += c
            addition[ins[p]+p[1]] += c
    pairs_counts = addition

letter_counts = Counter()
letter_counts[FIRST] += 1; letter_counts[LAST] += 1 # Don't double count ends
for pair, c in pairs_counts.items():
    l1, l2 = pair
    letter_counts[l1] += c
    letter_counts[l2] += c

most, least = max(letter_counts.values()), min(letter_counts.values())
print((most - least) // 2) # Remove double counts