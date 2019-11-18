import csv
import time
import tkinter as tk
from tkinter import filedialog

from CompareStrings import CompareStrings

start_time = time.time()

    #              TO DO
    #  Validate the data better (Example below)
    #  Think About custom confgis for new payers
    # 
    #
    # 
    #
    # Improvements Needed For Accuracy!
    # Remove the useless words or characters below and also only allow results for full words. No 'or' matches "ordering"
    # unnesacaryWords = ["the", "a", "?", "!", ".", "be", ""]
    # secondValidationRow = [word for word in rejectionMessageSplit not in unnesacaryWords]


def getExcel ():    
    import_file_path = filedialog.askopenfilename()

    with open(import_file_path) as newRejectionsFile:
        inputReadNewRejectionFile = list(csv.reader(newRejectionsFile, delimiter=','))
    
    return inputReadNewRejectionFile

def StartGUI():
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
    canvas1.pack()
        
    browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=browseButton_Excel)




def Runprogram():
#Set Variables
    newLineASCIIValues = (chr(10) + chr(10))
    currentRejectionRowCounter = 0 
    newRejectionRowCounter = 0
    counter = 0
    readCurrentRejectionFileList = []

#Read CSV Files
    with open('AHIN.csv') as newRejectionsFile, open('Combined_Analysis_2.csv') as currentRejectionsFile, open('Results.csv', "w", newline='') as resultsFile :
        readNewRejectionFile = (getExcel())
        readCurrentRejectionFile = list(csv.reader(currentRejectionsFile, delimiter=','))
        readResultsFile = csv.writer(resultsFile)

        readCurrentRejectionFileList = readCurrentRejectionFile


        readResultsFile.writerow(['Rejection Checked'] + ['Rejection Found'] + ['Row #'] +["FormattedAccuracy"] + ["ErrorCode"])

#Iterates over each row in New Reject File, assigning it an index    
        for row in readNewRejectionFile:
            newRejectionRowCounter = newRejectionRowCounter + 1
            
        #Reset the Object after writing it to Results File
            ClosestRow = {"Row" : 0, "RejectionChecked": "", "RejectionFound": "", "Accuracy": 0, "ErrorCode": ""}

        #Sets currentRow to current iterated Row at Col 35
            currentRow = row[35]

        #Custom for AHIN Edit 
        #Seperate Claim Rejection from notes into list
        #Only pull the claim rejection for list 
            firstValidationIteratedRow = currentRow.split(newLineASCIIValues, -1)
            firstValidationIteratedRow = firstValidationIteratedRow[0]
        
        #This will seperate each iteration of a full claim rejection (for testing)
            #print("====--------------------====")
            #print(firstValidationIteratedRow)
            
        #Iterates over each row in Current Reject File, assigning it an index
            for rows in readCurrentRejectionFileList:
                errorCode = rows[1]
                currentOldRow = rows[4]
                currentRejectionRowCounter = currentRejectionRowCounter + 1
            #Checks Accuracy of Two Strings
                accuracyOfCurrentString = CompareStrings(str(firstValidationIteratedRow), str(currentOldRow))
            #Sets Object to the most correct value
                if accuracyOfCurrentString > ClosestRow["Accuracy"]:
                    #print(accuracyOfCurrentString)
                    ClosestRow["Accuracy"] = accuracyOfCurrentString    
                    ClosestRow["FormattedAccuracy"] = "{:.0%}".format(accuracyOfCurrentString)
                    ClosestRow["Row"] = newRejectionRowCounter
                    ClosestRow["RejectionChecked"] = firstValidationIteratedRow
                    ClosestRow["RejectionFound"] = currentOldRow
                    ClosestRow["ErrorCode"] = errorCode

            readResultsFile.writerow([ClosestRow["RejectionChecked"]] + [ClosestRow["RejectionFound"]] + [ClosestRow["Row"]] +[ClosestRow["FormattedAccuracy"]] +[ClosestRow["ErrorCode"]])        
            print(newRejectionRowCounter)
            
    end_time = time.time()
    print("Program ran for %g seconds" % (end_time - start_time))       
    print(newLineASCIIValues)


def main(): 
    StartGUI()
    Runprogram()

main()

# print("Compare Strings should return 33%")
# CompareStrings("Address is missing", "NM109 is not correct") # => 33%