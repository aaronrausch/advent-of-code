
with open('inputs/2020-12-08.txt') as raw_instructions:

    cleaned_instructions = [instruction.rstrip('\n')
                            for instruction in raw_instructions.readlines()]

    instructions = []
    for instruction in cleaned_instructions:
        instruction_tuple = instruction.split(' ')
        opcode, value = instruction_tuple
        instructions.append((opcode, value))

# PART 1
accumulator = 0
index = 0
visited = []

running = True
while running:
    try:
        opcode, value = instructions[index]
        value = int(value)
    except IndexError:
        print(
            f'Program completed successfully. Accumulator finished at: {accumulator}')
        running = False

    if index in visited:  # instruction visited before; machine stuck in infinite loop
        print(f'Program stuck in loop. Accumulator finished at: {accumulator}')
        running = False

    visited.append(index)

    # opcode cases
    if opcode == 'nop':
        index += 1  # ignore any value, if present

    elif opcode == 'acc':
        accumulator += value
        index += 1

    elif opcode == 'jmp':
        index += value
