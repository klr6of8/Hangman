import random

class Hangman:
    def __init__(self):
        wordsFile = open("mylist.txt", 'r')
        wordsList = wordsFile.read().split("\n")
        number = random.randint(0,len(wordsList))
        self.word = wordsList[number]
        self.guessedLetters = []
        self.max_guesses = 6
        self.guesses_left = self.max_guesses
        
        
    def get_display_string(self):
        letters = []
        for letter in self.word:
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


                


