# 1.
x = 5
y = 10
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("oooo needs some work")

# 1 will result in the 2nd print statement, since 2 * x is equal to 10, not greater than.

# 2.
x = 5
y = 10
if len("Dog") < x:
    print("Question 2 works!")
else:
    print("Still missing out")

# 2 will result in the first print statement, since the length of "Dog" (3) is less than x (5)

# 3.
x = 2
y = 5
if (x ** 3 >= y) and (y ** 2 < 26):
    print("GOT QUESTION 3!")
else:
    print("Oh good you can count")

# 3 will result in the first print statement since:
# x^3 = 8, which is greater than y (5)
# AND y^2 = 25, which is less than 26

# 4.
name = "Dan"
group_one = ["Greg", "Tony", "Susan"]
group_two = ["Gerald", "Paul", "Ryder"]
group_three = ["Carla", "Dan", "Jefferson"]

if name in group_one:
    print(name + " is in the first group")
elif name in group_two:
    print(name + " is in group two")
elif name in group_three:
    print(name + " is in group three")
else:
    print(name + " does not have a group")

# 4 will result in the 3rd print statement, since "Dan" is in group_three

# 5.
height = 66
age = 16
adult_permission = True

if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars")
else:
    print("Stick to lazy river")

# 5 will result in the 4th print statement, since:
# the age is too low for the first 3, but adult_permission is true