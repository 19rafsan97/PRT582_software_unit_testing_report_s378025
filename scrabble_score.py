"""
This module implements a Scrabble score calculator along with additional
features such as validating input, enforcing word length constraints, and
checking the validity of words using a dictionary. It is designed with
Test-Driven Development (TDD) in mind, and uses nltk library for word
validation.
"""

import time
import random
import nltk
from nltk.corpus import words
nltk.download('words')


# Define a dictionary for letter values in Scrabble
LETTER_VALUES = {
    **dict.fromkeys("AEIOULNRST", 1),
    **dict.fromkeys("DG", 2),
    **dict.fromkeys("BCMP", 3),
    **dict.fromkeys("FHVWY", 4),
    **dict.fromkeys("K", 5),
    **dict.fromkeys("JX", 8),
    **dict.fromkeys("QZ", 10),
}

# Download the valid words dictionary from nltk corpus
VALID_WORDS = set(words.words())


def calculate_score(word: str) -> int:
    """
    Calculate the Scrabble score for a given word.

    Args:
        word (str): The word for which the score will be calculated.

    Returns:
        int: The total Scrabble score of the word.

    Raises:
        ValueError: If the input contains non-alphabetic characters.
    """
    if not word.isalpha():
        raise ValueError("Input must be alphabetic")

    word = word.upper()  # Convert to uppercase to match the LETTER_VALUES
    return sum(LETTER_VALUES[letter] for letter in word)


def validate_word_length(word: str, length: int) -> bool:
    """
    Validate if the word length matches the required length.

    Args:
        word (str): The word to validate.
        length (int): The required length of the word.

    Returns:
        bool: True if the word length is correct, False otherwise.
    """
    return len(word) == length


def is_valid_word(word: str) -> bool:
    """
    Check if a word is valid by confirming it exists in the dictionary.

    Args:
        word (str): The word to check for validity.

    Returns:
        bool: True if the word is valid, False otherwise.
    """
    return word.lower() in VALID_WORDS


def prompt_user_for_word() -> str:
    """
    Prompt user to input a word with a specific length and a 15-second timer.

    The length of the word is randomly generated, and the user must provide
    a word of that length within the time limit. If the user exceeds the time
    or enters an incorrect length, the function will prompt again. The user
    can also enter 'quit' to exit the game.

    Returns:
        str: The word input by user that meets the requirements or 'quit'
        to exit.

    Raises:
        TimeoutError: If the user exceeds the 15-second time limit.
    """
    length = random.randint(4, 8)
    print(f"Please enter a word of length {length}. You have 15 seconds.")
    print("Enter 'quit' to exit the game at any time.\n")

    start_time = time.time()
    user_input = input()  # Get input from the user
    end_time = time.time()

    # Check if the input time exceeded 15 seconds
    if end_time - start_time > 15:
        raise TimeoutError("Time limit exceeded!")

    if user_input.lower() == 'quit':
        return 'quit'

    # Validate if the word length matches the required length
    if not validate_word_length(user_input, length):
        print(f"Word must be {length} characters long.")
        return prompt_user_for_word()

    return user_input


def play_scrabble_game():
    """
    Play a round-based Scrabble game where user inputs words to score points.

    The game consists of multiple rounds where user is asked to enter a word
    of a randomly generated length. The word is validated for its length, and a
    score is calculated based on Scrabble letter values. The game keeps going
    until 10 rounds are completed, the user chooses to quit, or the user exits.

    After each round, the total score is displayed, and once the game ends,
    the final score is presented.
    """
    total_score = 0
    round_count = 0

    while round_count < 10:
        try:
            word = prompt_user_for_word()  # Prompt for a word from the user

            if word == 'quit':
                print(f"You chose to quit. Your total score is {total_score}.")
                break

            # Validate if the word is in the dictionary
            if not is_valid_word(word):
                print("Invalid word. Try again.")
                continue

            # Calculate and display the word's score
            score = calculate_score(word)
            print(f"Word score: {score}")
            total_score += score
            round_count += 1

        except ValueError as ve:
            print(f"Error: {ve}")
        except TimeoutError as te:
            print(f"Error: {te}")

    if round_count == 10:
        print(f"Game over. Your total score is {total_score}.")


if __name__ == "__main__":
    # Start the Scrabble game if the script is executed directly
    play_scrabble_game()
