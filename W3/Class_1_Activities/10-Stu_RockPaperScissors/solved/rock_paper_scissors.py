# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Check that player gave valid answer
while user_choice not in options:
    user_choice = input("Please input \"r\", \"p\", or \"s\"! ")

# Run Conditionals
print(f"The computer picked {computer_choice}")
# Selected same option
if user_choice == computer_choice:
    print("It's a draw!")
# Player wins
elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
    print("You won!")
# Computer Wins
else:
    print("The computer won!")


# could use index to do a cleaner looking if table
# userindex - cpuindex = 1 or -2 on win
                        # 0 on tie
                        # -1 or 2 on loss
# # get that #
# indexCheck = options.index(user_choice) - options.index(computer_choice)
# # Selected same option
# if user_choice == computer_choice:
#     print("It's a draw!")
# # Player wins
# elif (indexCheck == 1) or (indexCheck == -2):
#     print("You won!")
# # Computer Wins
# else:
#     print("The computer won!")