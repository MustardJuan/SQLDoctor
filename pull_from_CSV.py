import csv

def pull_from_CSV():

    dictionary = {}

    # goes through each line in the pre-made oayloads and creates the dcitionary to transport
    with open('fullpayloads.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            dictionary[row[0]] = row[2]

    return dictionary
