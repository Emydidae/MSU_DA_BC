import csv
import os

# grab csv path and output path
budget_path = os.path.join('Resources/budget_data.csv')
output_path = os.path.join('analysis/budget_analysis.txt')
# variables to store desired info
# profit refers to both profit and loss, used just profit for readability
month_total = 0
profit_net = 0
profit_change = []
profit_avg_change = 0
profit_max_change_i = 0
profit_min_change_i = 0
profit_max_change = []
profit_min_change = []
# variables to store lists of the csv data
month_list = []
profit_list = []


# open our csv and read into a reader
with open(budget_path, encoding="utf8") as budget_csv:
    budget_reader = csv.reader(budget_csv, delimiter=",")
    # skip header row
    header = next(budget_reader)

    # move data to a temporary list so we can iterate through it multiple times to break
    # it up and calculate stats one at a time instead of all at once in a huge loop
    budget_list = [row for row in budget_reader]
    # split month data to separate list
    month_list = [row[0] for row in budget_list]
    # split profit / loss data to separate list
    profit_list = [int(row[1]) for row in budget_list]


# calculate # of months by tallying the rows in the table
month_total = len(profit_list)

# calculate net profit by summing the profit / loss column
profit_net = sum(profit_list)

# calculating the change in profit month-to-month
# iterate through indexes such that the final index will be the penultimate value in the profit list
for i in range(len(profit_list) - 1):
    # calculate and append the change from the current index to the next, as well as the month
    profit_change.append([profit_list[i + 1] - profit_list[i], month_list[i + 1]])

# calculate average change in profits
profit_avg_change = round(sum([item[0] for item in profit_change]) / len([item[0] for item in profit_change]), 2)

# get index for max and min change in profits, so we can easily pull that data
for i in range(len(profit_change)):
    if profit_change[i][0] > profit_change[profit_max_change_i][0]:
        profit_max_change_i = i
    if profit_change[i][0] < profit_change[profit_min_change_i][0]:
        profit_min_change_i = i
# pull max / min change in profits
profit_max_change = profit_change[profit_max_change_i]
profit_min_change = profit_change[profit_min_change_i]


# create / format analysis
analysis = (f'Financial Analysis\n\
----------------------------\n\
Total Months: {month_total}\n\
Total: ${profit_net}\n\
Average Change: ${profit_avg_change}\n\
Greatest Increase in Profits: {profit_max_change[1]} (${profit_max_change[0]})\n\
Greatest Decrease in Profits: {profit_min_change[1]} (${profit_min_change[0]})')
# print analysis to terminal
print(analysis)
# open output file
with open(output_path, "w") as output:
    # write analysis to file
    output.write(analysis)
