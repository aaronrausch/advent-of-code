
import re

with open('inputs/2020-12-16.txt') as file_input:

    f = [l for l in file_input.read().splitlines()]
    your = f.index('your ticket:') + 1
    nearby = f.index('nearby tickets:') + 1
    sr = 0
    er = your - 2

    rules = []
    for l in f[sr:er]:
        r = [int(n) for n in re.findall(r'\d+', l)]
        rules.append(r[0:2])
        rules.append(r[2:4])

def validity(number):
    valid = False
    for rule in rules:
        if number >= rule[0] and number <= rule[1]:
            valid = True
    return valid

invalid_score = 0
tickets = f[nearby:]

for ticket in tickets:
    values = [int(n) for n in re.findall(r'\d+', ticket)]
    for v in values:
        if not validity(v):
            invalid_score += v
            # tickets.remove(ticket)

print(invalid_score)
