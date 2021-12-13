
import re

with open('inputs/2021-12-13.txt') as file:
    data = file.read().splitlines()
    DOTS_START, DOTS_END, INS_START, INS_END = 0, 982, 983, 995
    dots, instructions = data[:DOTS_END], data[INS_START:]
    dots = [dot.split(',') for dot in dots]
    dots = [(int(x),int(y)) for x, y in dots]

def create_paper(dots):
    x_axis = max(x for x, _ in dots) + 1
    y_axis = max(y for _, y in dots) + 1
    paper = [['.' for _ in range(x_axis)] for _ in range(y_axis)]
    for dot in dots:
        x, y = dot
        paper[y][x] = '#'
    return paper

def horizontal_fold(paper):
    for i, row in enumerate(paper[number:]):
        for j, _ in enumerate(row):
            if paper[number - i][j] == '.':
                paper[number - i][j] = paper[number + i][j]
    paper = paper[:number]
    return paper

def vertical_fold(paper):
    for i, row in enumerate(paper):
        for j, _ in enumerate(row[number:]):
            if paper[i][number - j] == '.':
                paper[i][number - j] = paper[i][number + j]
    paper = [row[:number] for row in paper]
    return paper

def count_dots(paper):
    return sum(sum(1 if d == '#' else 0 for d in row) for row in paper)

def pretty_print(paper):
    for row in paper:
        print(''.join('#' if d == '#' else ' ' for d in row))

paper = create_paper(dots)
for instruction in instructions:    # For part 1, instructions[:1]

    axis = re.search(r'x|y', instruction).group()
    number = int( re.search(r'\d+', instruction).group() )

    match axis:
        case 'y': paper = horizontal_fold(paper)
        case 'x': paper = vertical_fold(paper)

print(count_dots(paper))
pretty_print(paper)