import os

with open("mydata2.txt", encoding="utf-8") as myFile:

    lineNum = 1

    while True:

        line = myFile.readline()

        if not line:
            break

        print("line", lineNum)

        # split()
        wordList = line.split()

        # len()
        print("Number of words :", len(wordList))

        #Loop count characters in the word list
        charCount = 0

        for word in wordList:
            for char in word:
                charCount += 1

        #Divide character count / len word list
        avgNumChars = charCount/len(wordlist)

        print("Avg word length : {:.2}.format(avgNumChars))

        lineNum += 1
