
from collections import Counter

with open('inputs/2021-12-03.txt') as input_file:
    file = [_ for _ in input_file.read().splitlines()]
    file_copy = file.copy()


BINARY_LENGTH = len(file[0])

# PART 1
gamma, epsilon = '', ''

for i in range(BINARY_LENGTH):

    bits = [b[i] for b in file]
    counts = Counter(bits)

    if counts['1'] > counts['0']:
        gamma += '1'
        epsilon += '0'
    elif counts['0'] > counts['1']:
        gamma += '0'
        epsilon += '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma * epsilon)

# PART 2
oxygen, co2 = 0, 0

for i in range(BINARY_LENGTH):

    # OXYGEN
    bits = [b[i] for b in file]
    counts = Counter(bits)

    if counts['1'] >= counts['0']:
        file = [b for b in file if b[i] == '1']
    else:
        file = [b for b in file if b[i] == '0']

    if len(file) == 1:
        oxygen = file[0]

    # CO2
    bits = [b[i] for b in file_copy]
    counts = Counter(bits)

    if counts['1'] >= counts['0']:
        file_copy = [b for b in file_copy if b[i] == '0']
    else:
        file_copy = [b for b in file_copy if b[i] == '1']

    if len(file_copy) == 1:
        co2 = file_copy[0]

oxygen = int(oxygen, 2)
co2 = int(co2, 2)
print(oxygen * co2)
