# John Hopkins 
# Version 6
# PyPoll HomeWork

import os
import csv
import collections
from collections import Counter

print (f'\n')  
print (f' executing... ') 

# Create lists
voters_candidates = []
vote_per_candidate = []

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join('Resources', 'election_data.csv')

# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    # Read through each row of data after the header
    for row in csv_reader:
        voters_candidates.append(row[2])

    # Sort the list by default ascending order
    sorted_list = sorted(voters_candidates)

    #count votes per candidate in most common outcome order and append to a list
    count_candidate = Counter (sorted_list) 
    vote_per_candidate.append(count_candidate.most_common())

    # calculate the percentage of votes per candidate in 3 digital points
    for item in vote_per_candidate:
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')

# -->>  Export a text file with the results
election_file = os.path.join("Results.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{vote_per_candidate[0][0][0]}: {first}% ({vote_per_candidate[0][0][1]})\n")
    outfile.write(f"{vote_per_candidate[0][1][0]}: {second}% ({vote_per_candidate[0][1][1]})\n")
    outfile.write(f"{vote_per_candidate[0][2][0]}: {third}% ({vote_per_candidate[0][2][1]})\n")
    outfile.write(f"{vote_per_candidate[0][3][0]}: {fourth}% ({vote_per_candidate[0][3][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {vote_per_candidate[0][0][0]}\n")
    outfile.write("-------------------------\n")    

#Print out final message to terminal
finalMessage = (" Results.txt file created successfully ")

print (f'\n')           
print (f'*****************************************')
print (f'')
print (f'"{finalMessage}"')
print (f'')
print (f'*****************************************')
print (f'\n') 