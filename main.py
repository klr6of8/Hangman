from hangman import *
hangmanGame = Hangman()
previous_num_guesses_left = 0 
keepplaying = True
while(keepplaying):
   
    print(hangmanGame.get_display_string())
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print(f"Must be one letter. You have {num_guesses_left} guesses left.")
        continue
    num_guesses_left = hangmanGame.guess(guess)
    display_string = hangmanGame.get_display_string()
    if num_guesses_left == -1:
        print(f"You already guessed {guess}")
        num_guesses_left = previous_num_guesses_left
    else:
        previous_num_guesses_left = num_guesses_left


    # if there are no underscores left, then we must have won
    if "_" not in display_string:
        print(f"YOU WON!! The word was: '{hangmanGame.word}'")
    elif num_guesses_left == 0:
        print(f"You lost :( The word was: '{hangmanGame.word}'")
    else:
        print(display_string)
        print(f"You have {num_guesses_left} guesses left""\n")
        continue


    nextgame = input("Would you like to play again?")
    if nextgame != "yes" and nextgame != "y":
        keepplaying = False
    else:
        hangmanGame = Hangman()
        previous_num_guesses_left = 0 