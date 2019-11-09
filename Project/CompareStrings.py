def CompareStrings(string1, string2):
    counter = 0
    wordCounter = 0
    #The sentences should not be case senstive
    CaptialString1 = string1.upper()
    CaptialString2 = string2.upper()
    newLineASCIIValues = (chr(10) + chr(10))
    splitString1 = CaptialString1.split(" ")

    for word in splitString1:
        wordCounter += 1

    #Check For Word In String And If True Add To Counter
        if CaptialString2.find(word) != -1:
            # print("The word: ")
            # print(word)
            # print("is Found in the sentence")
            # print(CaptialString2)
            # print(chr(10) + chr(10))
            counter = counter + 1
    
    MatchPercentage = (counter / len(splitString1))

    # print(wordCounter)

    # print(splitString1)
    # print("COMPARED TO")
    # print(string2, "IS")
    # print("{:.0%}".format(MatchPercentage))
    # print("----------------")
    # print(newLineASCIIValues)
    return(MatchPercentage)




#TEST CASES 
# print("Should equal 100%")
# CompareStrings("testing this string", "This string is testing stuff") # => 100%

# print("Should equal 33%")
# CompareStrings("Address is missing", "NM109 is not correct") # => 33%
