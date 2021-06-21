import os
import csv

read_path = os.path.join("resources", "election_data.csv")
write_path = os.path.join("analysis", "election_analysis.csv")

total = 0
canidates = []
high = 0
winner = ""
results = {}

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
        print(canidate)
    
        
# print(f'\n{results}\n')

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


















