# exercise 2
# develop a game where it will show a scrambled word
# and the user will need to guess it.
# at the end, the word will be shown at the screen
# and if the user have guessed it right or not.

import random

words = ["kernel", "motherboard", "programming", "languages"]


def scrambleWordGame():
    print("\nalright, let's play a game.")
    print("i'll show you a word and you need to guess it.")
    print("okay, let's go!\n")

    word = random.choice(words)
    scrambled = "".join(random.sample(word, len(word)))

    print(scrambled)
    response = input("what's your guess? -> ")

    print(f"\nthe word is {word}")
    if response == word:
        print("you have guessed it right, congrats!")
    else:
        print("that's not correct, good luck next time!")


scrambleWordGame()
