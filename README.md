

This is a simple Python implementation of the classic Hangman game. In this game, the player has to guess the letters of a hidden word. The player starts with a set number of lives and loses a life for each incorrect guess. The game continues until the player either guesses all the letters in the word or runs out of lives.
Features

    Randomly selects a word from a predefined list.
    Displays the current state of the word with guessed letters and underscores.
    Allows the player to guess letters one at a time.
    Tracks and displays the number of lives remaining.
    Notifies the player if they have won or lost the game.

Installation

This project does not require any special libraries or installations. It uses Python's standard library.
Usage

    Run the game:

    Open your terminal or command prompt, navigate to the directory where the script is located, and run the script using Python.

    bash

    python hangman.py

    Gameplay:
        The game will display the current state of the word with underscores for unguessed letters.
        Input a letter to make a guess.
        The game will inform you if your guess is correct or incorrect and update the number of lives accordingly.
        Continue guessing letters until you either guess the entire word or run out of lives.

Example

When you start the game, you might see something like this:

less

Current word: _ _ _ _ _
Write a letter: a

If 'a' is in the word, it will be revealed:

arduino

Current word: _ a _ _ _

If 'a' is not in the word, you will lose a life:

css

Uhoh, you have 9 lives left

The game ends when you either:

    Guess the word correctly, and you see a message like:

Congrats You win!! 
The movie was avatar

Or run out of lives, and you see a message like:

    You lost, the movie was avatar

Code Explanation

    Word Selection: The game selects a random word from a predefined list.
    Guess Handling: The game updates the displayed word based on correct guesses and reduces the number of lives on incorrect guesses.
    Win/Loss Conditions: The game checks if the player has guessed the entire word or if lives have been exhausted to determine the outcome.

Contributing

Feel free to submit improvements or bug fixes through pull requests. For major changes, please open an issue to discuss them first.
