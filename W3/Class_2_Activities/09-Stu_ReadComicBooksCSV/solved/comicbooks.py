# Modules
import os
import csv

# Prompt user for title lookup
titleLookup = input('Please input a title to look up: ').lower()

# Set path for file
csvpath = os.path.join("..", "Resources", "comic_books.csv")

# Set variable to check if we found the video
bookFound = False

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header
    next(csvreader)

    # Loop through looking for the video
    for row in csvreader:
        # check both possible titles
        if row[0].lower() == titleLookup or row[1].lower() == titleLookup:
            # Set variable to confirm we have found the video
            bookFound = True
            print(f'{row[0]} was published by {row[8]} in {row[9]}.')

    # If the book is never found, alert the user
    if not bookFound:
        print('Sorry, we couldn\'t find your book.')