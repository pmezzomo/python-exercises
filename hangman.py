# Hangman game: randomly picks a word and lets the player guess letters or the full word

import random


def get_word():
    word_list = ['cat', 'dog', 'lizard', 'centipede', 'butterfly']
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_progress = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 5

    print(f"HANGMAN!\nHint: {len(word)} letters!")
    print(display_hangman(tries))
    print(word_progress)
    print()

    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already tried:", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_progress)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_progress = ''.join(word_as_list)
                if '_' not in word_progress:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already tried the word:", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_progress = word
        else:
            print("Invalid input.")

        print(display_hangman(tries))
        print(word_progress)
        print()

    if guessed:
        print("Congratulations! You guessed the word! You win!")
    else:
        print("You lost! The word was:", word)


def display_hangman(tries):
    stages = [
        """
           ---------
           |        |
           |        o
           |       \\|/
           |        |
           |       / \\
           .
        """,
        """
           ---------
           |        |
           |        o
           |       \\|/
           |        |
           |       /
           .
        """,
        """
           ---------
           |        |
           |        o
           |       \\|/
           |        |
           |
           .
        """,
        """
           ---------
           |        |
           |        o
           |       \\|
           |        |
           |
           .
        """,
        """
           ---------
           |        |
           |        o
           |        |
           |        |
           |
           .
        """,
        """
           ---------
           |        |
           |        o
           |
           |
           |
           .
        """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N) ").upper() == 'Y':
        word = get_word()
        play(word)


main()
