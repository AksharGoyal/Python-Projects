# Hangman  

Your favourite game Hangman is back! The program uses 2 files: hangman.py and words.py.  
words.py contains English words, with no punctuations, from which we pick a word and then start the game.  
The goal is to find the right alphabets that make the word before our man gets executed.  

We have 9 chances and using 9 chances, we want to guess the right word that can prevent the execution. When we run the program, we are prompted to enter an alphabet. Below output shows how it starts:  
```
Guess a letter: I
You have used these letters: I
Current word: - - - - - - - - I - -
Guess a letter:
```
We guessed the right alphabet so nothing happened to our man but we managed to get closer to the right word. If our guess was wrong, below is what would have been our output after our input:  
```
Guess a letter: Z

        |
        |
        |
        |
        |
        |

You have used these letters: Z
Current word: - - - - - - -
Guess a letter:
```
We made a wrong guess so our man gets closer to executed. Note that whether our guess is right or wrong, it will get stored in a set that let us know which alphabets we have already used. The below output shows what happens when we reuse an alphabet:  
```
You have used these letters: Z
Current word: - - - - - - -
Guess a letter: Z
Letter already used! Try again.
You have used these letters: Z
Current word: - - - - - - -
Guess a letter:
```

In the below example, when you can run the program and eventually run out of chances to save the man, we get the ouput that we lost. The actual word is revealed and the executed man is shown too.
```
You have used these letters: O I U M G F A R L
Current word: O - - R -
Guess a letter: N
         ____________
        |       |
        |      ( )
        |     --|--
        |       |
        |      / \
        |

You lost! The word was OVERT!
```  

If you choose to play this game, make sure to have both words.py and hangman.py together since hangman.py needs words.py to choose a valid English word for the game. Hope you enjoy :)
