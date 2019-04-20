import csv

def pull_from_CSV():
    # dbNameList = []
    # fingerprintList = []
    # payloadList = []

    dictionary = {}

    with open('ExploitDb_-_FinExRX.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            dictionary[row[0]] = row[2]

            # dbNameList.append(row[0])
            # fingerprintList.append(row[1])
            # payloadList.append(row[2])

    # print("DB NAMES: ")
    # for x in dbNameList:
    #     print("         " + x)
    
    # print()
    # for x in fingerprintList:
    #     print(x)

    # print()
    # print("PAYLOADS:")
    # for x in payloadList:
    #     print("       " + x)

    # return dbNameList, payloadList
    return dictionary

pull_from_CSV()


