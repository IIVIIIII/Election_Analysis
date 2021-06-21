import os
import csv

# set paths for csv to read and txt to write
read_path = os.path.join("resources", "budget_data.csv")
write_path = os.path.join("analysis", "budget_analysis.txt")


# set variables for results to calculate
total = 0
greatincrease_n = 0
greatdecrease_n = 0
monthcount = 0
month = ""
greatincrease_m = ""
greatdecrease_m = ""

# read csv and analyise data
with open(read_path, 'r') as bank_data:

    bank_read = csv.reader(bank_data)
    
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


# write results of analysis to a txt file
analysis = open(write_path, 'w')
analysis.write("Financial Analysis\n")
analysis.write("----------------------------\n")
analysis.write("Total Months: " + str(monthcount) + "\n")
analysis.write("Total: $" + str(total) + "\n")
analysis.write("Average Change: " + str(average) + "\n")
analysis.write("Greatest Increase in Profits: " + str(greatincrease_m) + " ($" + str(greatincrease_n) + ")\n")
analysis.write("Greatest Decrease in Profits: " + str(greatdecrease_m) + " ($" + str(greatdecrease_n) + ")\n")
analysis.close

# print results of analysis to terminal
print("\nFinancial Analysis")
print("----------------------------")
print("Total Months: " + str(monthcount))
print("Total: $" + str(total))
print("Average Change: " + str(average))
print("Greatest Increase in Profits: " + str(greatincrease_m) + " ($" + str(greatincrease_n) + ")")
print("Greatest Decrease in Profits: " + str(greatdecrease_m) + " ($" + str(greatdecrease_n) + ")\n")








