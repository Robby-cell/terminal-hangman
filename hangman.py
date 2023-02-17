
# used the following because i had no idea how to draw a stick man 🤷‍♂️
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

from random import choice
from json import dumps
import sys


def startRandomGame(): #  starts a new game
    _running = True

    display()

    while _running:
        checkOver()
        guessv()
        checkGuess()
        display()


def gameInit():
    
    global failed 
    failed = 0

    global letters
    letters = 'abcdefghijklmnopqrstuvwxyz'

    global word
    word = initializeWord()

    global letterFail
    letterFail = []

    global letterTried
    letterTried = []

    global guess
    guess = '0'

    global _running
    _running = False


    global wordDict
    wordDict = {}
    for letter in word:
        if letter != '_':
            wordDict.update({letter: '_'})
        else:
            wordDict.update({letter: ' '})

    ####
    for key in wordDict:
        if wordDict[key] != '_':
            print(key)
        else:
            print('f')

    print(dumps(wordDict))
    ####

    guess = 'h'
    try:
        wordDict[guess]
        print('good')

    except KeyError as e:
        print('bad')


    global HANGMANPICS 
    HANGMANPICS = [f'''
  +---+
  |   |
      |
      |
      |         {'failed tries:'} {letterFail}
      |
=========''', f'''
  +---+
  |   |
  O   |
      |
      |         {'failed tries:'} {letterFail}
      |
=========''', f'''
  +---+
  |   |
  O   |
  |   |
      |         {'failed tries:'} {letterFail}
      |
=========''', f'''
  +---+
  |   |
  O   |
 /|   |
      |         {'failed tries:'} {letterFail}
      |
=========''', f'''
  +---+
  |   |
  O   |
 /|\  |
      |         {'failed tries:'} {letterFail}
      |
=========''', f'''
  +---+
  |   |
  O   |
 /|\  |
 /    |         {'failed tries:'} {letterFail}
      |
=========''', f'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |         {'failed tries:'} {letterFail}
      |
=========''']
    


def initializeWord(): # initialize whats needed for the game to play out
    words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

    word = choice(words)

    return word


def guessv(): # take a guess
    
    sys.stdout.buffer.write('make a guess: '.encode('utf8'))
    guess = input().lower()[0]

    if guess in letterTried:
        guessv()

    elif not letters.find(guess):
        guessv()

    else:
        checkGuess()


def checkGuess(): # ...
    return


def duplicateGuess():
    return


def goodGuess():
    #
    return


def badGuess():
    failed += 1
    letterFail.append(guess)
    letterTried.append(guess)


def display():
    sys.stdout.buffer.write(f"{HANGMANPICS[failed]}".encode('utf8'))
    for key in wordDict:
        sys.stdout.buffer.write(wordDict[key].encode('utf8'))


def checkOver():

    for key in wordDict:
        if key != wordDict[key]:
            print(key)
            return

    _running = False


if __name__ == '__main__':

    failed = 0
    letters = 'abcdefghijklmnopqrstuvwxyz'
    word = initializeWord()
    letterFail = []
    letterTried = []
    guess = '0'
    _running = False


    wordDict = {}
    for letter in word:
        if letter != '_':
            wordDict.update({letter: '_'})
        else:
            wordDict.update({letter: ' '})

    ####
    for key in wordDict:
        if wordDict[key] != '_':
            print(key)
        else:
            print('f')

    print(dumps(wordDict))
    ####

    guess = 'h'
    try:
        wordDict[guess]
        print('good')

    except KeyError as e:
        print('bad')


    HANGMANPICS = [f'''
  +---+
  |   |
      |
      |
      |         {'failed tries:'} {letterFail}
      |
=========''', f'''
  +---+
  |   |
  O   |
      |
      |         {'failed tries:'} {letterFail}
      |
=========''', f'''
  +---+
  |   |
  O   |
  |   |
      |         {'failed tries:'} {letterFail}
      |
=========''', f'''
  +---+
  |   |
  O   |
 /|   |
      |         {'failed tries:'} {letterFail}
      |
=========''', f'''
  +---+
  |   |
  O   |
 /|\  |
      |         {'failed tries:'} {letterFail}
      |
=========''', f'''
  +---+
  |   |
  O   |
 /|\  |
 /    |         {'failed tries:'} {letterFail}
      |
=========''', f'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |         {'failed tries:'} {letterFail}
      |
=========''']
    
    startRandomGame()
