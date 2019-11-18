# This Removes unnessecary words 
# 
#

unnessecaryWords = ["THE", "\n", "OR", "CLAIM", "/", "'", "", "WE", "THIS", ]

def BasicValidation(string1):
    splitString1 = string1.split(" ")
    
    for word in splitString1:
        if word.upper() in unnessecaryWords:
            splitString1.remove(word)

    validatedString = ' '.join(splitString1)
    return validatedString