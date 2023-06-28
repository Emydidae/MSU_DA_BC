# Create a variable called 'name' that holds a string
name = input('What is your name? ')
# Create a variable called 'country' that holds a string
country = input('What country do you live in? ')
# Create a variable called 'age' that holds an integer
age = int(input('What is your age? '))
# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = int(input('What is your hourly wage? '))
# Calculate the daily wage for the user
daily_wage = hourly_wage * 8
# Create a variable called 'satisfied' that holds a boolean
satisfied = bool(input('Are you satisfied? (True / False) '))
# Print out "Hello <name>!"
print('Hello ' + name + '!')
# Print out what country the user entered
print('Country: ' + country)
# Print out the user's age
# end statement here just makes it so it doesn't go to the next line at the end of the first print
print('Age: ', end = '')
print(age)
# With an f-string, print out the daily wage that was calculated
print(f'Your daily wage is {daily_wage}')
# With an f-string, print out whether the users were satisfied
if satisfied:
    print('You were satisfied.')
else:
    print('You were not satisfied.')