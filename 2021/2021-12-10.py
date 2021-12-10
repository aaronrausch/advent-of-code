
with open('inputs/2021-12-10.txt') as i:
    f = [l for l in i.read().splitlines()]

def score_part_1(lst):
    dct = {')': 3, ']': 57, '}': 1_197, '>': 25_137}
    return sum(dct[i] for i in lst)

def score_part_2(lst):
    dct = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for inc in lst:
        score = 0
        for b in inc:
            score *= 5
            score += dct[b]
        scores.append(score)

    # Return middle value of sorted array
    scores = sorted(scores)
    index = (len(scores)-1) // 2
    return scores[index]

pairs = dict(zip('{[(<','}])>'))
part_one, part_two = [], []
for line in f:
    stack = []
    for b in line:
        if b in pairs:
            stack.append(b)
        else:
            if b != pairs[stack.pop()]:
                part_one.append(b)
                break
    else:
        if stack:
            inc = [pairs[b] for b in stack[::-1]]
            part_two.append(inc)

print(score_part_1(part_one))
print(score_part_2(part_two))