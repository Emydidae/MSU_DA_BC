# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
for i in range(len(candy_list)):
    print(f'[{i}] {candy_list[i]}')


# Select candies by allowance
# for i in range(allowance):
#     # Variable to hold input
#     user_num = int(input('Pick a candy by inputting its index number (0-8): '))
#     # Check for good answer
#     while user_num not in range(len(candy_list)):
#         user_num = int(input('Make sure to only input a number from 0 to 8. Try again: '))
#     # Add to list
#     candy_cart.append(candy_list[user_num])

# Select candies until no more
keep_picking = 'y'
while keep_picking == 'y':
    # Variable to hold input
    user_num = int(input('Pick a candy by inputting its index number (0-8): '))
    # Check for good answer
    while user_num not in range(len(candy_list)):
        user_num = int(input('Make sure to only input a number from 0 to 8. Try again: '))
    # Add to list
    candy_cart.append(candy_list[user_num])
    # Prompt to try again
    keep_picking = input('Pick another candy? ("y" or "n") ')
    while keep_picking not in ['y','n']:
        keep_picking = input('Make sure to input "y" or "n". Try again: ')

# Print Result
print('You got:')
for i in candy_cart:
    print(i)