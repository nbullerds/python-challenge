import csv
import os
import statistics

totalVotes = 0
winnerCount = 0
winner = ""

# Read in csv file of profit/losses data and ignore the first line
pypoll_csv = os.path.join("Resources","02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")
with open(pypoll_csv) as pypoll_csv:
    csvreader = csv.reader(pypoll_csv, delimiter=',')
    next(pypoll_csv)
    listVotes, uniqueVotes = [], []
    for row in csvreader:
        # Put the information we need from the file into a list for analysis
        listVotes.append(row[2])

        # Count the total number of votes
        totalVotes = totalVotes + 1

pypoll_csv.close()

# Create a list of unique votes
for x in listVotes: 
    if x not in uniqueVotes: 
        uniqueVotes.append(x)

#Output to output file
outputFile = open(os.path.join("Analysis", "02-Homework_03-Python_PyPoll_Analysis.txt"),"w")
outputFile.write(f"Election Results" + "\n")
outputFile.write(f"----------------------------"+"\n")
outputFile.write(f"Total Votes: {totalVotes}" + "\n")
outputFile.write(f"----------------------------"+"\n")
for value in uniqueVotes:
    outputFile.write(f"{value}: {round(((listVotes.count(value)/totalVotes) * 100), 4)}% ({listVotes.count(value)})" + "\n")
    if listVotes.count(value) > winnerCount:
        winnerCount = listVotes.count(value)
        winner = value
outputFile.write(f"----------------------------"+"\n")
outputFile.write(f"Winner: {winner}"+"\n")

outputFile.close()

#Output to terminal
readFile = open(os.path.join("Analysis", "02-Homework_03-Python_PyPoll_Analysis.txt"),"r")
Lines = readFile.readlines()
for line in Lines:
    print(f"{line}")