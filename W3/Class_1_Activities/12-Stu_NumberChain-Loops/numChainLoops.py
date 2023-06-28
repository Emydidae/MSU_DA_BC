# Using a `while` loop, ask the user "How many numbers?", and then print out a chain of numbers in increasing order, from 0 to the user-input number.

# After the results have been printed, ask the user if they would like to continue.

    # If "y" is entered, keep the chain running by inputting a new number and starting a new count from 0 to the new user-input number.

    # If "n" is entered, exit the application.


keepLooping = 'y'

while keepLooping == 'y':
    # get user input for # chain length
    chainLength = int(input('Input how many numbers should be in the chain: '))
    
    # print chain
    for i in range(chainLength):
        print(i)
    
    # ask to continue, automatically lowercase it
    keepLooping = input('Print another number chain? (y/n) ').lower()

    # make sure answer is valid, ask again if not
    while keepLooping not in ['y','n']:
        keepLooping = input('Please input either "y" or "n". ').lower()

# upon exiting loop
print('All done.')