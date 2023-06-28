# Print Hello User!
print('Hello User!')

# Take in User Input
userIn = input('Hey say something real quick. ')

# Respond Back with User Input
if userIn == 'something real quick.':
    print('Nice')
else:
    print(f'You said {userIn}. I told you to say "something real quick."')

# Take in the User Favorite Number
userNum = int(input('What\'s your favorite number? '))

# Respond Back with a statement based on your favorite number
if userNum == 5:
    print('Nice')
else:
    print(f'Well, {userNum} is okay, but it\'s not 5.')