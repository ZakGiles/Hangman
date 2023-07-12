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
    WinLoss = 0

    liGuessedLetters = []

    print('''welcome to hangman''')

    # Pick random word from word list
    word = words[random.randint(1,len(words)-1)][0].upper()
    print()
    print(man[0])
    print()

    # Underscores for number of letters in word
    hiddenWord = []
    for l in word:
        if l == " ":
            hiddenWord.append(" ")
        else:
            hiddenWord.append("_")

    print("Word:", ' '.join(hiddenWord))
    print("\nIncorrect letters:")
    
    wordAfterGuesses = hiddenWord

    # Game loop
    gameGoing = True
    while gameGoing == True:
        
        if len(liGuessedLetters) == 7:
            WinLoss = -1
            break

        validGuess = False
        while validGuess == False:
            guess = input("\nGuess a letter: ").lower()

            if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
                screen_clear()
                print()
                print(man[len(liGuessedLetters)])
                print()
                print(' '.join(wordAfterGuesses))
                print("\nIncorrect letters:", ', '.join(str(c) for c in liGuessedLetters))
                print("\nyou need to guess a letter")

            elif guess.upper() in liGuessedLetters or guess.upper() in wordAfterGuesses:
                screen_clear()
                print()
                print(man[len(liGuessedLetters)])
                print()
                print(' '.join(wordAfterGuesses))
                print("\nIncorrect letters:", ', '.join(str(c) for c in liGuessedLetters))
                print("\nyou already guessed that")
            
            else:
                validGuess = True

        screen_clear()

        print()
        print(man[len(liGuessedLetters)])

        guess = guess.upper()

        if guess in word:
            # Replace underline in word with letter that is correctly guessed
            indexesOfLetters = [c for c in range(len(word)) if word.startswith(guess, c)]
            for x in range(len(word)):
                if x in indexesOfLetters:
                    wordAfterGuesses[x] = guess
            
        # If all letters are known, the game is won
        if '_' not in wordAfterGuesses:
            WinLoss = 1
            break

        # Add incorrect guesses to incorrect guesses list
        if guess not in word:
            liGuessedLetters.append(guess)

        # Show incorrect guesses
        print()
        print(' '.join(wordAfterGuesses))
        print("\nIncorrect letters:", ', '.join(str(c) for c in liGuessedLetters))

    # Game lose and game win messages
    if WinLoss == -1:
        screen_clear()
        print()
        print(man[len(liGuessedLetters)])
        print()
        print(' '.join(wordAfterGuesses))
        print("\nIncorrect letters:", ', '.join(str(c) for c in liGuessedLetters))
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