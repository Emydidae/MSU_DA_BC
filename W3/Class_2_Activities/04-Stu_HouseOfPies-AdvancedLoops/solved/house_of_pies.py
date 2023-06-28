
# menu variable
pieMenu = ['Pecan','Apple Crisp','Bean','Banoffee','Black Bun','Blueberry','Buko','Burek','Tamale','Steak']

# display menu
print('Welcome to the House of Pies! Here are our pies:')
print('---------------------------------------------------------------------')
# could hard-code this part, this shows how you could print it with a changing menu tho
for i in range(len(pieMenu)):
    if i < (len(pieMenu) - 1):
        print(f'({i + 1}) {pieMenu[i]}', end = ', ')
    else:
        print(f'({i + 1}) {pieMenu[i]}')
print('---------------------------------------------------------------------')

# actual order part of the code
orderAgain = 'y'
piesOrdered = 0

# bonus - makes a list matching length of menu, 0 for each value
pieReceipt = []
for i in range(len(pieMenu)):
    pieReceipt.append(0)

while orderAgain == 'y':
    # ask for pie number, automatically adjust to list index
    pieNum = int(input('Please input the number of the pie you would like to order: ')) - 1

    # print response, increase number of pies purchased by 1
    print(f'Great! We\'ll have that {pieMenu[pieNum]} right out for you!')
    piesOrdered += 1

    # bonus - add to tally of the pie bought
    pieReceipt[pieNum] += 1

    # ask if they want to order again, make sure they say 'y' or 'n'
    orderAgain = input('Would you like to get another pie? (y / n): ').lower()
    while orderAgain not in ['y','n']:
        orderAgain = input('Please input either "y" or "n": ').lower()

# upon loop ending
print('---------------------------------------------------------------------')
print('Your Receipt:')
print('---------------------------------------------------------------------')

# bonus - print individual pie tallies
for i in range(len(pieMenu)):
    print(f'{pieMenu[i]} - {pieReceipt[i]}')

# print total
print('---------------------------------------------------------------------')
print(f'Total: {piesOrdered} Pies')