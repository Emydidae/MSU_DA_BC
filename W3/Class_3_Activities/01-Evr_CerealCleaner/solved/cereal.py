import os
import csv

cereal_csv = os.path.join("..", "Resources/cereal_bonus.csv")

with open(cereal_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    header = next(csv_reader)

    for row in csv_reader:
        if float(row[7]) >= 5:
            print(row[0], row[7])