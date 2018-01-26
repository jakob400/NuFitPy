import csv

with open('output.csv', newline='') as myFile:
    reader = csv.DictReader(myFile, delimiter = '/', quoting=csv.QUOTE_NONE)
    #writer = csv.DictWriter(myFile, delimiter = '/', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)
