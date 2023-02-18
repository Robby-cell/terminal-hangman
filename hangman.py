
# used the following because i had no idea how to draw a stick man 🤷‍♂️
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

from random import choice
import sys


def initializeWord(): # initialize whats needed for the game to play out

    # potentially add some bot that will grab a word from the dictionary or maybe make it multiplayer or a file containing words

    words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

    return choice(words)


_word = initializeWord()

toPrint = '_'*len(_word)
    
letters = "abcdefghijklmnopqrstuvwxyz"
    
letterFail = []
    
letterTried = []
    
guess = ''
    
_running = False
    
myWord = [letter for letter in _word]

    
HANGMANPICS = ['''
  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========''', '''
  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========''', '''
  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========''', '''
  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========''', '''
  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========''', '''
  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========''', '''
  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========''']


def guessv(): # take a guess

    global guess
    global letterTried
    
    sys.stdout.buffer.write('make a guess: \n'.encode('utf8'))
    guess = input().lower()[0]

    if guess in letterTried:
        guessv()

    elif not letters.find(guess) + 1:
        guessv()

    else:
        checkGuess()


def checkGuess(): # ...

    global guess
    global letterTried
    global letterFail
    global toPrint
    global myWord

    indices = [i for i, e in enumerate(myWord) if guess == e]

    if len(indices) == 0:
        letterFail.append(guess)
        letterTried.append(guess)
        return
        
        
    for i in indices:
        toPrint = toPrint[:i] + guess + toPrint[i+1:]

    letterTried.append(guess)


def display():

    global letterFail
    global toPrint
    global HANGMANPICS

    sys.stdout.buffer.write(f"{HANGMANPICS[len(letterFail)]}\n".encode('utf8'))
    sys.stdout.buffer.write(f'Failed letters: {[letter for letter in letterFail]}\n'.encode('utf8'))

    sys.stdout.buffer.write(f'{toPrint}\n'.encode('utf8'))


def win():

    global _word

    display()

    sys.stdout.buffer.write(f'\n\nYou correctly guessed the word {_word}!\n'.encode('utf8'))
    exit()


def lose():

    global _word

    display()

    sys.stdout.buffer.write(f'\n\nYou failed to guess the word {_word} correctly!\n'.encode('utf8'))
    exit()


def checkOver():

    global letterFail
    global toPrint

    if len(letterFail) >= 6:
        lose()

    if not ('_' in toPrint):
        win()


def startRandomGame(): #  starts a new game

    global _running

    _running = True

    while _running:
        
        display()
        guessv()
        checkOver()
        


if __name__ == '__main__':

    startRandomGame()
