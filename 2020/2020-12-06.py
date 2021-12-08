
with open('inputs/2020-12-06.txt') as raw_votes_data:
    votes_data = [vote.replace('\n', '')
                  for vote in raw_votes_data.read().split('\n\n')]

sum_of_counts = 0
for vote in votes_data:
    sum_of_counts += len(set(vote))
print(sum_of_counts)
