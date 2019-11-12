def getGuessedWord(secretWord, lettersGuessed):
    string = ""
    for letters in secretWord:
        if letters in lettersGuessed:
            string += letters
        elif letters not in lettersGuessed:
            string += "_"
    return string
