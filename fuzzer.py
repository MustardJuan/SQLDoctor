import csv

def pull_from_generator():

    print("Starting Fuzzer!")
    
    fuzzingList = []
    fuzzingDict = {}
    dbList = []

    # Open Fuzzing Payloads and add them to a fuzzinglist and fuzzing Dictionary 
    with open('fuzzingLists/fuzz.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            hold = ""

            item_count = 0
            dbName = ""
            # add each item of every row to a dict and a list
            for item in row:
                if (item_count == 0):
                    dbName = item
                    dbList.append(dbName)
                    fuzzingDict[item] = ""

                    item_count += 1
                    continue
                
                hold = hold + " " + item
            
            #strips away white space
            fuzzingDict[dbName] = hold.strip()
            fuzzingList.append(hold.strip())

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

        #itemList is the complete CSV content that is split by spaces
        itemList = item.split()
        
        #we take the number of indexes
        countItemList = len(itemList)   

        #In the dictionary the key is the database name + payload then a number that is incrementing and the value is the whole row
        fuzzingDict[dbName + " payload:" + str(0)] = itemList

        #First spliting of the SQL statements
        firstpartfirst, secondpartfirst = itemList[:len(itemList)//2], itemList[len(itemList)//2:]
        
        fuzzingDict[dbName + " payload:" + str(1)] = firstpartfirst 
        fuzzingDict[dbName + " payload:" + str(2)] = secondpartfirst

        firstparthold = firstpartfirst
        secondparthold = secondpartfirst
        payloadCount = 3

        #loop generates entire dictionary of fuzzed input
        while(len(firstparthold) > 1 and len(secondparthold) > 1):
            
            #we create a variable to remain stateful 
            firstparthold = firstpartfirst
            
            #the first half of the payload is saved to the dictionary and then we increment the payload count
            firstpartfirst = firstpartfirst[:len(firstpartfirst)//2] 
            fuzzingDict[dbName + " payload:" + str(payloadCount)] = firstpartfirst
            payloadCount += 1

            #the first half of the second half of the payload is saved to the dictionary and then we increment the payload count
            secondparthold = secondpartfirst
            secondpartfirst = secondpartfirst[:len(secondpartfirst)//2] #split second half 
            fuzzingDict[dbName + " payload:" + str(payloadCount)] = secondpartfirst
            payloadCount += 1

            #similarily in the same logic applies to the 2nd parts of both but without the statefulness
            
            firstpartsecond = firstparthold[len(firstparthold)//2:]
            fuzzingDict[dbName + " payload:" + str(payloadCount)] = firstpartsecond
            payloadCount += 1

            secondpartsecond = secondparthold[len(secondparthold)//2:] 
            fuzzingDict[dbName + " payload:" + str(payloadCount)] = secondpartsecond
            payloadCount += 1
            
    # removes dictionary brackets so the input will be processed correctly
    for key,value in fuzzingDict.items():
        hold = ""
        for item in value:
            hold = hold + " " + item
        fuzzingDict[key] = hold

    return fuzzingDict       