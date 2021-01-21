import csv
import os
import statistics

monthCount, totalprofitCount, previousValue = 0, 0, 0

# Read in csv file of profit/losses data and ignore the first line
pybank_csv = os.path.join("Resources","02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")
with open(pybank_csv) as pybank_csv:
    csvreader = csv.reader(pybank_csv, delimiter=',')
    next(pybank_csv)
    #change_dict = {}
    listChange, listDates = [], []
    for row in csvreader:
        # Calculate the total profit/losses for the dataset
        currentValue = int(row[1])
        totalprofitCount = totalprofitCount + currentValue
              
        # create list of dates and list of changes in profit/losses for analysis
        valueChange = currentValue - previousValue
        listDates.append(row[0])
        listChange.append(valueChange)
        #change_dict.update({row[0] : valueChange})
        previousValue = currentValue

        # Count number of months in profit/losses data
        monthCount = monthCount + 1

pybank_csv.close()

# analysis needed for output (note removing first line for "change" metric as no value is known prior to what is in the dataset)
averageChange = round(statistics.mean(listChange[1:]),2)
greatestIncrease = round(max(listChange[1:]),2)
greatestDecrease = round(min(listChange[1:]),2)

#Output to output file
outputFile = open(os.path.join("Analysis", "02-Homework_03-Python_PyBank_Analysis.txt"),"w")
outputFile.write(f"Financial Analysis" + "\n")
outputFile.write(f"----------------------------"+"\n")
outputFile.write(f"Total Months: {monthCount}")
outputFile.write(f"Total: {totalprofitCount}" + "\n")
outputFile.write(f"Average  Change: {averageChange}" + "\n")
outputFile.write(f"Greatest Increase in Profits: {listDates[listChange.index(greatestIncrease)]} ({greatestIncrease})" + "\n")
outputFile.write(f"Greatest Decrease in Profits: {listDates[listChange.index(greatestDecrease)]} ({greatestDecrease})")

#Output to terminal
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {monthCount}")
print(f"Total: {totalprofitCount}")
print(f"Average  Change: {averageChange}")
print(f"Greatest Increase in Profits: {listDates[listChange.index(greatestIncrease)]} ({greatestIncrease})")
print(f"Greatest Decrease in Profits: {listDates[listChange.index(greatestDecrease)]} ({greatestDecrease})")