
with open('inputs/2021-12-08.txt') as input_file:
    stream = input_file.read().splitlines()

total_sum = 0
for line in stream:

    line = line.split(' | ')
    raw, output = line[0].split(' '), line[1].split(' ')

    keys = [0] * 10
    for n in raw:
        match len(n):
            case 2: keys[1] = n
            case 4: keys[4] = n
            case 3: keys[7] = n
            case 7: keys[8] = n

    for n in raw:
        ns = set(l for l in n)
        match len(n), len(ns & set(keys[1])), len(ns & set(keys[4])):
            case 6,2,3: keys[0] = ns
            case 5,1,2: keys[2] = ns
            case 5,2,3: keys[3] = ns
            case 5,1,3: keys[5] = ns
            case 6,1,3: keys[6] = ns
            case 6,2,4: keys[9] = ns

    output_sum = 0
    for i, digit in enumerate(output):
        for key in keys:
            if set(digit) == set(key):
                output_sum += keys.index(key) * (10 ** (len(output) - i))
    total_sum += output_sum

print(total_sum)
