
with open('inputs/2021-12-06.txt') as file:
    data = [int(i) for i in file.read().split(',')]
    fish = {n: data.count(n) for n in range(9)}

DAYS = 256
for _ in range(DAYS):
    breed = fish[0]
    for i in range(8):
        fish[i] = fish[i + 1]
        fish[i + 1] = 0
    fish[6] += breed
    fish[8] += breed

print(sum(f for f in fish.values()))
