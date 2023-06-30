import csv
import os

# grab csv path and output path
budget_path = os.path.join('Resources/election_data.csv')
output_path = os.path.join('Results/election_results.txt')
# variables to store desired info
vote_total = 0
candidates = []
votes_per_candidate = []
votes_percent = []
winner_i = 0
winner = ''
# variable to store list of vote data
candidate_voted = []


# open our csv and read into a reader
with open(budget_path, encoding="utf8") as budget_csv:
    budget_reader = csv.reader(budget_csv, delimiter=",")
    # skip header row
    header = next(budget_reader)

    # move data to a temporary list so we can iterate through it multiple times to break
    # it up and calculate stats one at a time instead of all at once in a huge loop
    ballot_list = [row for row in budget_reader]
    # isolate which candidate was voted for on each ballot
    candidate_voted = [ballot[2] for ballot in ballot_list]


# get total number of votes
vote_total = len(candidate_voted)

# get name of each UNIQUE candidate - see #2 in readme for credit
[candidates.append(name) for name in candidate_voted if name not in candidates]

# calculate # of votes per candidate & percent of vote total
votes_per_candidate = [0 for name in candidates]
for i in range(len(candidates)): # there may be some way to do this with nested list comprehensions, but I think this is more readable
    votes_per_candidate[i] = sum([1 for name in candidate_voted if name == candidates[i]])
votes_percent = [round((num / vote_total) * 100, 3) for num in votes_per_candidate]

# zip values into list of lists
votes_final = [item for item in zip(candidates, votes_percent, votes_per_candidate)]

# find index of winning candidate (popular vote), so we can easily pull that data
for i in range(len(votes_final)):
    if votes_final[i][2] > votes_final[winner_i][2]:
        winner_i = i
# grab info for winner
winner = votes_final[winner_i][0]


# create / format results
analysis = (f'Election Results\n\
-------------------------\n\
Total Votes: {vote_total}\n\
-------------------------\n')
# iterates through each candidate's statistics, adding a line to the analysis
analysis += ''.join([f'{cand[0]}: {cand[1]}% ({cand[2]})\n' for cand in votes_final])
analysis += f'-------------------------\n\
Winner: {winner}\n\
-------------------------'

# print analysis to terminal
print(analysis)

# open output file
with open(output_path, "w") as output:
    # write analysis to file
    output.write(analysis)