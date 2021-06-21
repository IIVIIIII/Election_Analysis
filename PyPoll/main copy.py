import os
import csv


# set paths for csv to read and txt to write
read_path = os.path.join('resources', 'election_data.csv')
write_path = os.path.join('analysis', 'election_analysis.txt')


# set variables for results to calculate
results = {}
total = 0
high = 0
winner = ""


# read csv and analyise data
with open(read_path, 'r') as election_data:

    election_read = csv.reader(election_data)

    next(election_read, None)

    for row in election_read:
        total = total + 1
        if row[2] in results:
            results[row[2]]['votes'] = results[row[2]]['votes'] + 1
        else:
            results[row[2]] = {'votes': 1, 'percentage': 0}

    for canidate in results.keys():
        results[canidate]['percentage'] = '{:.2%}'.format(results[canidate]['votes']/total)


# write results of analysis to a txt file
analysis = open(write_path, 'w')
analysis.write('Election Results\n')
analysis.write('-------------------------\n')
analysis.write(f'Total Votes: {total}\n')
analysis.write('-------------------------\n')

for result in results:
    if results[result]['votes'] > high:
        winner = result
        high = results[result]['votes']
    analysis.write(f'{result}: {results[result]["percentage"]} ({results[result]["votes"]})\n')

analysis.write("-------------------------\n")
analysis.write(f'Winner: {winner}\n')
analysis.write('-------------------------')


# print results of analysis to terminal
print('\nElection Results')
print('-------------------------')
print(f'Total Votes: {total}')
print('-------------------------')

for result in results:
    print(f'{result}: {results[result]["percentage"]} ({results[result]["votes"]})')

print("-------------------------")
print(f'Winner: {winner}')
print('-------------------------\n')
