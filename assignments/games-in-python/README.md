
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a Hangman-style game in Python that uses loops, conditionals, user input, and string handling to let players guess letters and win or lose based on their performance.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create the game foundation by defining a list of possible words, randomly choosing one, and initializing the variables needed to track guessed letters and incorrect attempts.

#### Requirements
Completed program should:

- Define a list of possible words for the player to guess.
- Randomly select one word from the list at the start of the game.
- Initialize game state variables, including guessed letters, incorrect guesses count, and maximum allowed misses.

### 🛠️ Guess Processing and Progress Display

#### Description
Implement the main game loop to accept letter guesses, update the game state, and show the current progress of the hidden word.

#### Requirements
Completed program should:

- Prompt the player to enter one letter at a time.
- Reveal correctly guessed letters in the hidden word using `_` placeholders for missing letters.
- Track and display incorrect guesses remaining.
- Prevent duplicate guesses from affecting the game state incorrectly.

### 🛠️ End Game and Result Messages

#### Description
Complete the game by checking win/lose conditions and displaying a final message that tells the player whether they won or lost.

#### Requirements
Completed program should:

- End the game when the word is fully guessed or when the player runs out of attempts.
- Display a win message when the player guesses the word.
- Display a lose message and reveal the secret word when attempts are exhausted.

