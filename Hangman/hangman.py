# importing the required modules
from words import words
import random
import string

# the dictionary containing the status of hangman
hangman_lives = {
    0:  """
        """,
    1:  """
        |
        |
        |
        |
        |
        |
        """,
    2:  """
         ____________
        |
        |
        |
        |
        |
        |
        """,
    3:  """
         ____________
        |       |
        |
        |
        |
        |
        |
        """,
    4:  """
         ____________
        |       |
        |      ( )
        |
        |
        |
        |
        """,
    5:  """
         ____________
        |       |
        |      ( )
        |       |
        |       |
        |
        |
        """,
    6:  """
         ____________
        |       |
        |      ( )
        |       |
        |       |
        |      /
        |
        """,
    7:  """
         ____________
        |       |
        |      ( )
        |       |
        |       |
        |      / \\
        |
        """,
    8:  """
         ____________
        |       |
        |      ( )
        |     --|--
        |       |
        |      / \\
        |
        """
}

def hangman():
    # get a word to start the game
    word = (random.choice(words)).upper()
    while '-' in word or ' ' in word:
        word = (random.choice(words)).upper()
    
    # setup the variables that will change accordingly
    lives_lost = 0
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    user = set() # player's input will be added here
    
    # game ends when player has either provided all the correct letters
    # or the player has made the man hang himself
    while len(word_letters) > 0 and lives_lost != 8:
        
        guess = input("Guess a letter: ").upper() # Enter a letter
        if guess in (alphabet - user):            # If not already provided
            user.add(guess)
            if guess in word_letters:
                # if the player has provided the right letter,
                # the missing blanks are filled with that letter
                word_letters.remove(guess)
            else:
                # player provided the wrong letter
                # the man nears death
                lives_lost += 1
                print(hangman_lives[lives_lost]) # Show the man's status
                if lives_lost == 8:
                    break
                
        elif guess in user:                        # Else already provided the letter before
            print("Letter already used! Try again.")
        else:
            print("Invalid character! Try again.")  # if the palyer entered non-alpha character
        
        # Show the current letters found and the blanks to be missed
        print(f"You have used these letters: {' '.join(user)}")
        word_list = [letter if letter in user else '-' for letter in word]
        print(f"Current word: {' '.join(word_list)}")
        
    # Game ended becoz the man was hanged
    if lives_lost == 8:
        print("You lost! The word was {}!".format(word))
    # Game ended becoz player found the right word
    else:
        print("You guessed the word! The word was {}!".format(word))
    
hangman()