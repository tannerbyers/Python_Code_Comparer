import csv
import time
from CompareStrings import CompareStrings

start_time = time.time()

    #              TO DO
    # 
    # Have the object for found values update for each rejection message. 
    # Fix the both Row Counters (the last row being returned is higher than the excel file)
    # The above counter issue might have something to do with how the excel file is read(possible linebreak issue)
    # Have the python program spit out a new excel file with the data from the ClosestRow Object
    #
    # Improvements Needed For Accuracy!
    # Remove the useless words or characters below and also only allow results for full words. No 'or' matches "ordering"
    # unnesacaryWords = ["the", "a", "?", "!", ".", "be", ""]
    # secondValidationRow = [word for word in rejectionMessageSplit not in unnesacaryWords]

def Runprogram():

    #Read CSV Files
    with open('AHIN.csv') as newRejectionsFile, open('Combined_Analysis_2.csv') as currentRejectionsFile :
        readRejectionFile = csv.reader(newRejectionsFile, delimiter=',')
        readCurrentRejectionFile = csv.reader(currentRejectionsFile, delimiter=',')

    
    #Set Variables
        newLineASCIIValues = (chr(10) + chr(10))
        wordsInRejectionCounter = 0
        currentRejectionRowCounter = 0 
        newRejectionRowCounter = 0
        ClosestRow = {"Row" : 0, "RejectionChecked": "", "RejectionFound": "", "Accuracy": 0}


#Iterates over each row in New Reject File, assigning it an index    
        for row in readRejectionFile:
        #Sets currentRow to current iterated Row at Col 35
            currentRow = row[35]
            


        #Only check the first rows (for testing)
            newRejectionRowCounter = newRejectionRowCounter + 1
        #Seperate Claim Rejection from notes into list
            firstValidationIteratedRow = currentRow.split(newLineASCIIValues, -1)
        #Only pull the claim rejection for list 
            firstValidationIteratedRow = firstValidationIteratedRow[0]
        #This will seperate each iteration of a full claim rejection (for testing)
            # print("====--------------------====")
            # print(firstValidationIteratedRow)

#Iterates over each row in Current Reject File, assigning it an index
        for currentOldRow in currentRejectionsFile:
            currentRejectionRowCounter = currentRejectionRowCounter + 1
        #Checks Accuracy of Two Strings
            accuracyOfCurrentString = CompareStrings(str(firstValidationIteratedRow), str(currentOldRow))
        
        #Sets Object to the most correct value
            if accuracyOfCurrentString > ClosestRow["Accuracy"]:
                ClosestRow["Accuracy"] = accuracyOfCurrentString
                ClosestRow["Row"] = currentRejectionRowCounter
                ClosestRow["RejectionChecked"] = firstValidationIteratedRow
                ClosestRow["RejectionFound"] = currentOldRow

    print("Rejection Checked :", ClosestRow["RejectionChecked"])
    print(chr(10))
    print("Rejection Found :", ClosestRow["RejectionFound"])
    print(chr(10))
    print("Accuracy:", ClosestRow["Accuracy"])
    print("Row (This value seems to be incorrect):", ClosestRow["Row"])

    end_time = time.time()
    print("Program ran for %g seconds" % (end_time - start_time))       
    print(newLineASCIIValues)

Runprogram()

# print("Compare Strings should return 33%")
# CompareStrings("Address is missing", "NM109 is not correct") # => 33%