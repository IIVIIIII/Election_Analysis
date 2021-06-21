import os
import csv

# set paths for csv to read and txt to write
read_path = os.path.join("resources", "election_data.csv")
write_path = os.path.join("analysis", "election_analysis.txt")

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
        results[canidate]['percentage'] = "{:.2%}".format(results[canidate]['votes']/total)



# write results of analysis to a txt file
analysis = open(write_path, 'w')
analysis.write('Election Results\n')
analysis.write('-------------------------\n')
analysis.write(f'Total Votes: {total}\n')
analysis.write('-------------------------\n')

for result in results:
    analysis.write(f'{result}: {results[result]["percentage"]} ({results[result]["votes"]})\n')
    
    if results[result]['votes'] > high:
        winner = result
        high = results[result]['votes']

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










# with open(read_path, 'r') as election_data:

#     election_read = csv.reader(election_data)

#     next(election_read, None)

#     for row in election_read:
#         cans[row[2]]["Votes"] = cans[row[2]]["Votes"] + 1
#     for can in cans:
#         if cans[can]["Votes"] > high:
#             high = cans[can]["Votes"]
#             winner = can
#         cans[can]["Percent"] = "{:.3%}".format(cans[can]["Votes"]/float(total))
#         results.append(str(can)+": "+str(cans[can]["Percent"])+" ("+str(cans[can]["Votes"])+")")

#     print("Election Results")
#     print("-------------------------")
#     print("Total Votes: "+str(total))
#     print("-------------------------")
#     for result in results:
#         print(result)
#     print("-------------------------")
#     print("Winner: "+str(winner))
#     print("-------------------------")

# with open(write_path, 'w') as election_analysis:

#     election_write = csv.writer(election_analysis, delimiter=',')

#     election_write.writerow(["Election Results"])
#     election_write.writerow(["-------------------------"])
#     election_write.writerow(["Total Votes: "+str(total)])
#     election_write.writerow(["-------------------------"])
#     for result in results:
#         election_write.writerow([result])
#     election_write.writerow(["-------------------------"])
#     election_write.writerow(["Winner: "+str(winner)])
#     election_write.writerow(["-------------------------"])


















