# @TODO: Write a function that returns the arithmetic average for a list of numbers

def average(numList):
    avg = sum(numList) / len(numList)

    return avg
# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))

print(average([64,22,905]))