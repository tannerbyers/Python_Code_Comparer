unnecessaryWords = ["the", "be", "If", "is"]
validatedString = []
removedwords = []

TestString = "This is the test string"

def SpecialValidation(providedString):
    wordListfromProvidedString = providedString.split(" ")
    for word in wordListfromProvidedString:
        if word in unnecessaryWords :
            removedwords.append(word)
            # print("Removed " + word)
        else:
            print("Validated Entry " + word)    
            # validatedString.append(word)

# print(TestString)  
#SpecialValidation(TestString)