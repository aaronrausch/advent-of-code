
with open('inputs/2020-12-02.txt') as raw_data:
    all_passwords = [password for password in raw_data.read().splitlines()]


def data_collection(password):
    minmax, char, password = password.split()
    minimum, maximum = minmax.split('-')
    char = char[0]

    return [int(minimum), int(maximum), char, password]


# PART 1
def range_validation(password_data):
    minimum, maximum, char, password = password_data

    valid = True
    char_count = password.count(char)
    if char_count > maximum or char_count < minimum:
        valid = False

    return valid


def range_counts(passlist):
    validity_count = 0
    for passline in passlist:
        pass_data = data_collection(passline)
        if range_validation(pass_data):
            validity_count += 1

    return validity_count


print(range_counts(all_passwords))


# PART 2
def position_validation(password_data):
    position1, position2, char, password = password_data

    return (password[position1 - 1] == char) ^ (password[position2 - 1] == char)


def position_counts(passlist):
    validity_count = 0
    for passline in passlist:
        pass_data = data_collection(passline)
        if position_validation(pass_data):
            validity_count += 1

    return validity_count


print(position_counts(all_passwords))
