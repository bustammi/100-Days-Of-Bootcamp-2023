# Hangman Game

This is a classic implementation of hangman game in Python. It uses two external modules: `hangman_art` and `hangman_words`.

## Getting Started

To play the game, run the script and guess letters until you either fill in all the blanks with the correct letters, or you run out of lives.

## External Modules

The two external modules `hangman_art` and `hangman_words` are used in this game. `hangman_words` contains the word list for the game, and `hangman_art` contains the ASCII art for the game.

## Todos

There are five `TODO` items in the code that can be completed to enhance the game:

1. Update the word list to use the `word_list` from `hangman_words.py`.
2. Import the stages from `hangman_art.py` and make the error go away.
3. Import the logo from `hangman_art.py` and print it at the start of the game.
4. If the user has entered a letter they've already guessed, print the letter and let them know.
5. If the letter is not in the chosen word, print out the letter and let them know it's not in the word.
