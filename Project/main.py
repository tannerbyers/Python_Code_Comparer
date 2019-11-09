import csv
import time
from CompareStrings import CompareStrings

start_time = time.time()

    #              TO DO
    # Iterate over the CurrentEdits File, Compare the Words in the IteratedNewRejections to CurrentEdits Row 
    # Add Number of words appeared to object, return object that calculates the hightest scoring row and its row # 
    # Add categories for high likely the returned code is to match the newones (check how many words matched and distinguish by color the ones with very few vs ones with a lot)
    # 
    # Possible Improvement for accuracy. Remove useless "words" below and also only allow results for full words. No 'or' matches "ordering"
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
        ClosestRow = {"Row" : 0, "RejectionChecked": "", "Accuracy": 0}


#Iterates over each row in New Reject File, assigning it an index    
        for row in readRejectionFile:
        #Sets currentRow to current iterated Row at Col 35
            currentRow = row[35]
            


            #Only check the first rows (for testing)
            if newRejectionRowCounter < 10:
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
                    if currentRejectionRowCounter < 10:
                        
                        print(currentOldRow)
                        print(currentRejectionRowCounter)
                        currentRejectionRowCounter = currentRejectionRowCounter + 1
                    #Checks Accuracy of Two Strings
                        accuracyOfCurrentString = CompareStrings(str(firstValidationIteratedRow), str(currentOldRow))
                    
                    #Sets Object to the most correct value
                        if accuracyOfCurrentString > ClosestRow["Accuracy"]:
                            ClosestRow["Accuracy"] = accuracyOfCurrentString
                            ClosestRow["Row"] = currentRejectionRowCounter
                            ClosestRow["RejectionChecked"] = firstValidationIteratedRow
                    else:
                        currentRejectionRowCounter = currentRejectionRowCounter + 1




    
    end_time = time.time()
    print("Program ran for %g seconds" % (end_time - start_time))       
    print(newLineASCIIValues)
    print(ClosestRow)


Runprogram()

# print("Compare Strings should return 33%")
# CompareStrings("Address is missing", "NM109 is not correct") # => 33%