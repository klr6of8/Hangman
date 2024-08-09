import random

class Hangman:

    # the constructor with optional parameters for hard coded test cases
    def __init__(self,word=None,guesses=None):
        wordsFile = open("mylist.txt", 'r')
        wordsList = wordsFile.read().split("\n")
        if word: # test case is specifying word to use
            self.word = word
            self.guess_index = 0
        else: # use random word from wordsFile
            number = random.randint(0,len(wordsList))
            self.word = wordsList[number]
            self.index = None
            self.guess_index = None
        self.guessedLetters = []
        self.max_guesses = 6
        self.guesses_left = self.max_guesses
        self.guesses = guesses
        
    # returns the display string
    def get_display_string(self):
        letters = []
        for letter in self.word:
            # adds the letter to the display string
            if letter in self.guessedLetters:
                letters.append(letter)
            else:
                letters.append("_")
        return " ".join(letters)
    
    # returns -1 if guess has already been guessed
    # returns guesses left otherwise
    def guess(self, guess): 
        if guess not in self.guessedLetters:
            self.guessedLetters.append(guess)
            if guess not in self.word:
                self.guesses_left -= 1
        else:
            return -1
        return self.guesses_left


                


