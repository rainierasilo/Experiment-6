def getAvailableLetters (lettersGuessed):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    temp = ""
    for letters in alphabet:
        if letters not in lettersGuessed:
            temp += letters
    return temp
