import os
import csv

# Path to collect data from the Resources folder
graduation_csv = os.path.join('..','Resources/graduation_data.csv')

# Define the function and have it accept the 'state_data' as its sole parameter
def print_percentages(state_data):

    state = str(state_data[0])
    public_students = int(state_data[1])
    public_grads = int(state_data[2])
    nonprofit_students = int(state_data[3])
    nonprofit_grads = int(state_data[4])
    forprofit_students = int(state_data[5])
    forprofit_grads = int(state_data[6])

# Find the total students
    total_students = public_students + nonprofit_students + forprofit_students
# Find the total graduates
    total_grads = public_grads + nonprofit_grads + forprofit_grads
# Find the public school graduation rate
    public_grad_rate = public_grads / public_students
# Remember that some states do not have nonprofit or forprofit private schools
# Find the non-profit school graduation rate
    if nonprofit_students == 0:
        nonprofit_grad_rate = 0
    else:
        nonprofit_grad_rate = (nonprofit_grads / nonprofit_students)
# Find the for-profit school graduation rate
    if forprofit_students == 0:
        forprofit_grad_rate = 0
    else:
        forprofit_grad_rate = (forprofit_grads / forprofit_students)
# Calculate the overall graduation rate
    total_grad_rate = total_grads / total_students
# Print out the state's name and its graduation rates
    print(f'{state}\'s Graduation Rates:')
    print(f'Public: {public_grad_rate}')
    print(f'Nonprofit: {nonprofit_grad_rate}')
    print(f'For Profit: {forprofit_grad_rate}')
    print(f'Overall: {total_grad_rate}')

# Read in the CSV file
with open(graduation_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what state they would like to search for
    state_to_check = input("What state do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the state's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if state_to_check == row[0]:
            print_percentages(row)
