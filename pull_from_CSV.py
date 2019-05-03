import csv

def pull_from_CSV():

    dictionary = {}

    with open('ExploitDb_-_FinExRX.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            dictionary[row[0]] = row[2]

    return dictionary

pull_from_CSV()