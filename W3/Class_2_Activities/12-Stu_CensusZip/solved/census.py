import os
import csv

census_csv = os.path.join("..", "Resources", "census_starter.csv")

# Lists to store data
place = []
population = []
income = []
poverty_count = []
poverty_rate = []
county = []
state = []

# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(census_csv, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        # Add place
        place.append(row[0])
        # Add population
        population.append(row[1])
        # Add per capita income
        income.append(row[4])
        # Add poverty count
        poverty_count.append(row[8])
        # Determine poverty rate to 2 decimal places, convert to string
        row_pov_rate = int(row[8]) / int(row[1])
        row_pov_rate = str(round((row_pov_rate), 2))
        poverty_rate.append(row_pov_rate)
        # Split the place into county and state
        # .split splits up the string it's attached to by whatever's in the parentheses (or whitespace by default)
        row_place_split = row[0].split(", ")
        county.append(row_place_split[0])
        state.append(row_place_split[1])

# Zip lists together
# used https://realpython.com/python-zip-function/ as reference since we didn't touch on this in class
zipped_census = zip(place,population,income,poverty_count,poverty_rate,county,state)

# Set variable for output file
output_file = os.path.join("census_final.csv")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Place", "Population", "Per Capita Income", "Poverty Count", "Poverty Rate",
                    "County", "State"])

    # Write in zipped rows
    for row in zipped_census:
        writer.writerow(row)
