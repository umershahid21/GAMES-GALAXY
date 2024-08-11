# UMER'S GAME GALAXY

## Overview

This Python program features a collection of games and utilities. It includes:

1. **Snake Water Gun** - A game where the user plays against the computer in a game of Snake, Water, and Gun.
2. **Secret Language Maker** - A game that transforms a string based on its length.
3. **Kon Banega Crorepati (KBC)** - A quiz game based on the popular TV show.
4. **Random Password Generator** - Generates a random password.
5. **Guess the Number** - A game where the user guesses a randomly generated number.

## Functions

### `snake_water_gun()`
- **Purpose**: Play Snake Water Gun game.
- **Inputs**: User chooses 1 (Snake), 2 (Water), 3 (Gun), or 0 (Exit).
- **Outputs**: Displays the result of the game.

### `secret_language_maker()`
- **Purpose**: Convert a string based on its length.
- **Inputs**: User provides a string.
- **Outputs**: Reverses the string if it's short, otherwise appends the first letter to the end.

### `KBC`
- **Methods**:
  - `options()`: Displays game introduction and options.
  - `question()`: Asks a question and processes the user's answer.
  - `lifeline()`: Provides lifelines for the quiz.

### `random_password_generator()`
- **Purpose**: Generate a random password.
- **Outputs**: Displays a randomly generated password of length 12.

### `guess_the_number()`
- **Purpose**: Guess a randomly generated number between 1 and 100.
- **Inputs**: User provides guesses or 0 to quit.
- **Outputs**: Provides feedback on the guess and ends the game.

## Main Function

### `main()`
- **Purpose**: Provides a menu to choose and run games.
- **Inputs**: User selects a game from the menu or chooses to exit.
- **Outputs**: Runs the selected game or exits the program.

## Running the Program

1. **Execute**: Run the script to start the menu.
2. **Interact**: Follow prompts to play games or generate passwords.
3. **Exit**: Choose `0` from the menu to exit.

