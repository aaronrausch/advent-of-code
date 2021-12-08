
with open('inputs/2020-12-04.txt') as raw_data:

    users = raw_data.read().split('\n\n')


conditions = ["byr", "iyr", "eyr", "hgt",
              "hcl", "ecl", "pid"]  # "cid" not required

valid_passports = 0
for user in users:
    conditions_check = all(
        True if (condition in user) else False for condition in conditions)
    if conditions_check:
        valid_passports += 1

print(valid_passports)
