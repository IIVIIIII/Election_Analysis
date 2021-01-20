import os
import csv

read_path = os.path.join("Resources", "budget_data.csv")
write_path = os.path.join("analysis", "budget_analysis.csv")

with open(read_path, 'r') as bank_data:

    bank_read = csv.reader(bank_data)

    total = 0
    monthcount = 0
    greatincrease_n = 0
    greatdecrease_n = 0
    month = ""
    greatincrease_m = ""
    greatincrease_m = ""
    
    next(bank_read, None)

    for row in bank_read:
        total = total + int(row[1])
        if row[0] != month:
            month = row[0]
            monthcount = monthcount + 1
        if int(row[1]) > greatincrease_n:
            greatincrease_n = int(row[1])
            greatincrease_m = row[0]
        if int(row[1]) < greatdecrease_n:
            greatdecrease_n = int(row[1])
            greatdecrease_m = row[0]

    average = "${:.2f}".format(float(total)/monthcount)

with open(write_path, 'w') as bank_analysis:

    bank_write = csv.writer(bank_analysis, delimiter=',')

    bank_write.writerow(["Financial Analysis"])
    bank_write.writerow(["----------------------------"])
    bank_write.writerow(["Total Months: " + str(monthcount)])
    bank_write.writerow(["Total: $" + str(total)])
    bank_write.writerow(["Average Change: " + str(average)])
    bank_write.writerow(["Greatest Increase in Profits: " + str(greatincrease_m) + " ($" + str(greatincrease_n) + ")"])
    bank_write.writerow(["Greatest Decrease in Profits: " + str(greatdecrease_m) + " ($" + str(greatdecrease_n) + ")"])

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(monthcount))
print("Total: $" + str(total))
print("Average Change: " + str(average))
print("Greatest Increase in Profits: " + str(greatincrease_m) + " ($" + str(greatincrease_n) + ")")
print("Greatest Decrease in Profits: " + str(greatdecrease_m) + " ($" + str(greatdecrease_n) + ")")








