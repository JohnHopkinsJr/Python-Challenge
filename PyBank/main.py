# John Hopkins 
# Version 6
# PyBank HomeWork

import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open file at csvpath  :
with open (csvpath, newline="") as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=",")
    csv_headers = next(csv_reader, None)

# Initate a lists to hold monthly data
    months = []
    profit = []
# Read through data records
    for row in csv_reader:
        months.append(row[1])
        profit.append(int(row[1]))
    total_months = len(months)

# Get revenues
    revenues = 0
    i = 1
    for i in range(total_months):
        revenues = revenues + int(profit[i])
   
# Find change per month
    change = []
    j = 0
    k = 0
    for j in range (1, total_months):
        if j == 0:
            change.append(0)
        else:
            change.append(int(profit[j])-int(profit[k]))
            k += 1

# Calculate average, max and min changes
    average_month = ((sum(change))/(len(change)))
    max_change = max(change)
    min_change = min(change)
   
# Export results
exportpath = ("Results.txt")
with open(exportpath, "w") as textfile:
    textfile.write(f"* PyBank Report Results * \n")
    textfile.write(f'  ---------------------\n')
    textfile.write(f"Total Revenues: ${revenues}\n")
    textfile.write(f"Total # of Months: {total_months}\n")
    textfile.write(f"Average Monthly Change: ${round((average_month))}\n")
    textfile.write(f"Greatest Revenues Increase: ${max_change}\n")
    textfile.write(f"Greatest Revenues Decrease: ${min_change}\n")
    textfile.write(f"Trending Change: ${round((average_month))}\n")

#Print out final message to terminal
finalMessage = (" Results.txt file created successfully ")
               
print (f'*****************************************')
print (f'\n')
print (f'"{finalMessage}"')
print (f'\n')
print (f'*****************************************')