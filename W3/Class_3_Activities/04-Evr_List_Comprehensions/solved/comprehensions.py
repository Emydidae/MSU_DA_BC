# @TODO: Your code here
string = "bananarama"

# long convert
letters = []
for letter in string:
    letters.append(letter)

print(letters)

# short convert
letters = [letter for letter in string]

print(letters)

# used with caps
capLetters = [letter.upper() for letter in string]

print(capLetters)

# conditionals
temperatures = [85,23,56,86,96,65]
# filters to only 80+
hot_days = [temperature for temperature in temperatures if temperature > 80]

print(hot_days)

hot_days = ["YES" if temperature > 80 else "NO" for temperature in temperatures]

print(hot_days)