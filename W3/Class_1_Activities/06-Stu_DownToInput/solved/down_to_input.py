# Take input of you and your neighbor
userName = input('What is your name? ')
neighborName = input('What is your neighbor\'s name? ')
# Take how long each of you have been coding
userMonths = int(input('How many months have you been coding? '))
neighborMonths = int(input('How many months has your neighbor been coding? '))
# Add total month
totalMonths = userMonths + neighborMonths
# Print results
print(f'Between {userName} and {neighborName}, there is a combined {totalMonths} months of coding experience.')