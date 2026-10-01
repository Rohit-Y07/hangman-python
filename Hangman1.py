# Assignment 1 CS180, hangman.py
# Name: Rohit Kumar Yadav
# Collaborators (2 people max): Prince Gupta
# Time spent: 1 week

# Hangman Game
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    return all(letter in letters_guessed for letter in secret_word)


def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_ "
    return guessed_word


def get_available_letters(letters_guessed):
    available_letters = [letter for letter in string.ascii_lowercase if letter not in letters_guessed]
    return ''.join(available_letters)


def hangman(secret_word):
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("You have 3 warnings left.")
    print("-------------")

    while guesses_remaining > 0:
        print(f"You have {guesses_remaining} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        
        guess = input("Please guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses_remaining -= 1
                print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
        elif guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
        else:
            letters_guessed.append(guess)
            if guess in secret_word:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                guesses_remaining -= 2 if guess in "aeiou" else 1

        print("-------------")

        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses_remaining * len(set(secret_word))
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {total_score}")
            break
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


def match_with_gaps(my_word, other_word):
    my_word_stripped = my_word.replace(" ", "")
    if len(my_word_stripped) != len(other_word):
        return False
    for mw, ow in zip(my_word_stripped, other_word):
        if mw != "_" and mw != ow:
            return False
        elif mw == "_" and ow in my_word_stripped:
            return False
    return True


def show_possible_matches(my_word):
    matches = [word for word in wordlist if match_with_gaps(my_word, word)]
    if matches:
        print("Possible word matches are:", " ".join(matches))
    else:
        print("No matches found")


def hangman_with_hints(secret_word):
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("You have 3 warnings left.")
    print("-------------")

    while guesses_remaining > 0:
        print(f"You have {guesses_remaining} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        
        guess = input("Please guess a letter: ").lower()

        if guess == "*":
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif not guess.isalpha() or len(guess) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses_remaining -= 1
                print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
        elif guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses_remaining -= 1
                print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
        else:
            letters_guessed.append(guess)
            if guess in secret_word:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                guesses_remaining -= 2 if guess in "aeiou" else 1

        print("-------------")

        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses_remaining * len(set(secret_word))
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {total_score}")
            break
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


if __name__ == "__main__":
    # To test the game without hints, uncomment the following two lines
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)
    
    # To test the game with hints, uncomment the following two lines
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
