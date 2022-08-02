# exercise 3
# modify the anterior exercise, the words will be read from a file.
# the file will contain a single word per line.

import random


def getWords():
    words = []

    file = open("words.txt", mode="r")
    for word in file:
        words.append(word.strip())

    file.close()

    return words


def scrambleWordGame():
    print("\nalright, let's play a game.")
    print("i'll show you a word and you need to guess it.")
    print("okay, let's go!\n")

    words = getWords()

    word = random.choice(words)
    scrambled = "".join(random.sample(word, len(word)))

    print(scrambled)
    response = input("what's your guess? -> ")

    print(f"\nthe word is: {word}")
    if response == word:
        print("you have guessed it right, congrats!")
    else:
        print("that's not correct, good luck next time!")


scrambleWordGame()
