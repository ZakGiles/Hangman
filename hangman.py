import csv
import random
from os import system, name

# Pictures of the hanging man in a list
man = ['''
   +---+
       |
       |
       |
       |
       |
==========''','''
   +---+
   |   |
       |
       |
       |
       |
==========''', '''
   +---+
   |   |
   0   |
       |
       |
       |
==========''', '''
   +---+
   |   |
   0   |
   |   |
       |
       |
==========''', '''
   +---+
   |   |
   0   |
  /|   |
       |
       |
==========''', '''
   +---+
   |   |
   0   |
  /|\  |
       |
       |
==========''', '''
   +---+
   |   |
   0   |
  /|\  |
  /    |
       |
==========''', '''
   +---+
   |   |
   0   |
  /|\  |
  / \  |
       |
==========''']



file = open("words.csv", "r")
words = list(csv.reader(file, delimiter=","))
file.close()

# Clear the screen in terminal
def screen_clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux
   else:
    _ = system('clear')

# Hangman game 
def hangman():
    screen_clear()
    win_lose = 0

    list_guessed_letters = []

    print('Welcome to Hangman')

    # Pick random word from word list
    word = words[random.randint(1,len(words)-1)][0].upper()
    print()
    print(man[0])
    print()

    # Underscores for number of letters in word
    hidden_word = []
    for l in word:
        if l == " ":
            hidden_word.append(" ")
        else:
            hidden_word.append("_")

    print("Word:", ' '.join(hidden_word))
    print("\nIncorrect letters:")
    
    word_after_guesses = hidden_word

    # Game loop
    game_going = True
    while game_going == True:
        
        if len(list_guessed_letters) == 7:
            win_lose = -1
            break

        valid_guess = False
        while valid_guess == False:
            guess = input("\nGuess a letter: ").lower()

            if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
                screen_clear()
                print()
                print(man[len(list_guessed_letters)])
                print()
                print(' '.join(word_after_guesses))
                print("\nIncorrect letters:", ', '.join(str(c) for c in list_guessed_letters))
                print("\nyou need to guess a letter")

            elif guess.upper() in list_guessed_letters or guess.upper() in word_after_guesses:
                screen_clear()
                print()
                print(man[len(list_guessed_letters)])
                print()
                print(' '.join(word_after_guesses))
                print("\nIncorrect letters:", ', '.join(str(c) for c in list_guessed_letters))
                print("\nyou already guessed that")
            
            else:
                valid_guess = True

        screen_clear()

        print()
        print(man[len(list_guessed_letters)])

        guess = guess.upper()

        if guess in word:
            # Replace underline in word with letter that is correctly guessed
            indexes_of_letters = [c for c in range(len(word)) if word.startswith(guess, c)]
            for x in range(len(word)):
                if x in indexes_of_letters:
                    word_after_guesses[x] = guess
            
        # If all letters are known, the game is won
        if '_' not in word_after_guesses:
            win_lose = 1
            break

        # Add incorrect guesses to incorrect guesses list
        if guess not in word:
            list_guessed_letters.append(guess)

        # Show incorrect guesses
        print()
        print(' '.join(word_after_guesses))
        print("\nIncorrect letters:", ', '.join(str(c) for c in list_guessed_letters))

    # Game lose and game win messages
    if win_lose == -1:
        screen_clear()
        print()
        print(man[len(list_guessed_letters)])
        print()
        print(' '.join(word_after_guesses))
        print("\nIncorrect letters:", ', '.join(str(c) for c in list_guessed_letters))
        print()
        print('\nYOU LOST')
        print("The word was", word)
        print()
        print()
    else:
        print('\nYOU WON!!')
        print("The word was", word)
        print()
        print()


screen_clear()

while True:
    play = input("Play hangman? Y/N:")
    if play.lower() == "y":
      hangman()
    else:
        break