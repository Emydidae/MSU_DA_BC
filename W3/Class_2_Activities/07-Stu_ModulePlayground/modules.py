# this one doesn't have any specifics, so I don't have much
# the main modules I've used in the past are "random" and "time"
import random as r
import time as t
# importing them with "as ____" isn't necessary but makes it easier
# so you don't have to type as much in the prefix lol

# picks a random integer from given range
print(r.randint(0,55))

# picks a random value from the list
list = ['a','b','c','d','e']
print(r.choice(list))

# shuffles the list
r.shuffle(list)
print(list)

# picks a # of random values (without repeating)
print(r.sample(list, 3))

# more at https://docs.python.org/3/library/random.html#module-random

# this range function makes a range from 0 ending at 26, stepping 5 at a time (0,5,10,15,20,25)
for i in range(0,26,5):
    print(i)
    # sleep pauses for 1 second
    t.sleep(1)

# more at https://docs.python.org/3/library/time.html#module-time