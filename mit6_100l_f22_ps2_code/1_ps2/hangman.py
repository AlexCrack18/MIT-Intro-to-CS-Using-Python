# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed) -> string:
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess = ""
    for i in secret_word:
        if i in letters_guessed:
            guess += i
        else:
            guess += "*"
    return guess


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    available_letters = ""
    for letter in alphabet:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters

def letter_to_reveal(secret_word, letters_guessed):
  available_letters = get_available_letters(letters_guessed)
  choose_from = ""
  for letter in secret_word:
    if letter in available_letters:
      choose_from += letter

  new = random.randint(0, len(choose_from) - 1)
  return choose_from[new]

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    print(f"The secret word contains {len(secret_word)} letters")
    guesses = 10
    letters_guessed = ""
    
    while (guesses > 0):
      print("----------------------------------")
      
      print(f"You have {guesses} guesses")
      print(f"Available letters: {get_available_letters(letters_guessed)}")

      letter = input("Please guess a letter: ")
  
      if len(letter) != 1:
        print("Oops, that is an invalid guess, try again")
        continue

      if not letter.isalpha():
        if letter == "!" and with_help: 
          if guesses >= 3:
            letter = letter_to_reveal(secret_word, letters_guessed)
            print(f"Letter revealed: {letter}")
            guesses -= 3 
          else:
            print(f"There are fewer than 3 guesses available, help cannot be used: {get_word_progress(secret_word, letters_guessed)}") 
            continue
        else:
          print("Oops, that is an invalid guess, try again")
          continue
      
      letter = letter.lower()
      if letter in letters_guessed:
        print("You have already used this letter.")
        continue
      letters_guessed += letter
      if letter in secret_word:
        print("Good guess: ", end="")
      else:
        print("Oops, that letter is not in my word: ", end="")
        if letter in ("aeiou"):
          guesses -= 1
        guesses -= 1
      word_progress: string = get_word_progress(secret_word, letters_guessed)
      print(word_progress)
      if word_progress.isalpha():
        print("----------------------------------")
        print("Congratulations you won")
        print("Your total score: ", (guesses + 4 * len(set(secret_word)) + 3 * len(secret_word)))
        return
    
    print("----------------------------------")
    print(f"Sorry, you ran out of guesses. The word was {secret_word}")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    #secret_word = choose_word(wordlist)
    secret_word = "wildcard"
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

