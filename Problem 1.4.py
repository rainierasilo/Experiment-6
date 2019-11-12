def hangman(secretWord):
    print ("Welcome to the game, Hangman!")
    print ("In this game you will guess the mystery word, letter by letter! Goodluck!")
    print ("The mystery word is " + str(len(secretWord)) + " letters long.")
    
    lettersGuessed = ''
    guessesLeft = 10
   
    print ("------------")
    
    while True:
        print ("Guesses left: " + str(guessesLeft))
        print ("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Guess a letter: ")
        
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed += guess
            print ("Nice guess: " + getGuessedWord(secretWord, lettersGuessed))
        elif guess in lettersGuessed:
            print ("You've already guessed that: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guess
            print ("That letter is not here: " + getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1
        
        print ("------------")
        
        if guessesLeft <= 0:
            print ("Sorry, no more guesses left for you my dear. The word was " + secretWord + ".")
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print ("Amazing! You found out the mystery word! Congratulations!:)")
            break
        