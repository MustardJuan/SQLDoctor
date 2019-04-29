import csv
from POST_handler import *

def pull_from_generator():

    print("Starting Fuzzer!")
    
    fuzzingList = []
    fuzzingDict = {}
    dbList = []

    with open('fuzzingLists/fuzz.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            hold = ""
            if(line_count == 0):
                line_count += 1
                continue

            item_count = 0
            dbName = ""
            for item in row:
                if (item_count == 0):
                    dbName = item
                    dbList.append(dbName)
                    fuzzingDict[item] = ""

                    item_count += 1
                    continue
                
                hold = hold + " " + item
            
            fuzzingDict[dbName] = hold.strip()

            fuzzingList.append(hold.strip())
            line_count += 1    

        #return fuzzingDict
        return fuzzingList, dbList

def fuzz():
    
    returns = pull_from_generator()
    fuzzingList = returns[0]
    dbList = returns[1]

    fuzzingDict = {}

    count = 0
    for item in fuzzingList:
        dbName = dbList[count]
        count += 1

        itemList = item.split()
        countItemList = len(itemList)   

        fuzzingDict[dbName + " payload:" + str(0)] = itemList

        firstpart, secondpart = itemList[:len(itemList)//2], itemList[len(itemList)//2:]
        fuzzingDict[dbName + " payload:" + str(1)] = firstpart
        fuzzingDict[dbName + " payload:" + str(1)] = secondpart
        # print(firstpart)
        # print(secondpart)

        payloadCount = 2
        flag = 1 #Denotes which half to choose to go forward with
        while(len(firstpart) > 1 or len(secondpart) > 1):
            if(flag):
                firstpart, secondpart = firstpart[:len(firstpart)//2], firstpart[len(secondpart)//2:] #split first half
                fuzzingDict[dbName + " payload:" + str(payloadCount)] = firstpart
                payloadCount += 1
                fuzzingDict[dbName + " payload:" + str(payloadCount)] = secondpart
                payloadCount += 1
            else:
                firstpart, secondpart = secondpart[:len(firstpart)//2], secondpart[len(secondpart)//2:] #split second half 
                fuzzingDict[dbName + " payload:" + str(payloadCount)] = firstpart
                payloadCount += 1
                fuzzingDict[dbName + " payload:" + str(payloadCount)] = secondpart
                payloadCount += 1
            # print(firstpart)
            # print(secondpart)
            # print()
    
    for key,value in fuzzingDict.items():
        hold = ""
        for item in value:
            hold = hold + " " + item
        fuzzingDict[key] = hold

    return fuzzingDict       