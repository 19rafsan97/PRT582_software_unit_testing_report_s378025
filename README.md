# Scrabble Score Calculator

This project is a Scrabble score calculator implemented in Python. It allows users to calculate the Scrabble score of words, validate word lengths, and check word validity against a dictionary. The project also includes automated tests to ensure the correctness of the functionalities.

## Project Structure

- `scrabble_score.py`: Contains the main implementation of the Scrabble score calculator, word validation, and game logic.
- `test_scrabble.py`: Includes unit tests for the functions in `scrabble_score.py`.
- `requirements.txt`: Lists the required Python packages for the project.
- `README.md`: This file.

## Installation

To set up the project, follow these steps:

1. **Clone the Repository**

   ```sh
   git clone https://github.com/your-username/scrabble-score-calculator.git
   cd scrabble-score-calculator

2. **Install Dependencies**
Install the required Python packages listed in `requirements.txt`:

```
pip install -r requirements.txt
```
## Usage
To play the Scrabble game, run the following command:
```
python scrabble_score.py
```
The game will prompt you to enter words of specified lengths, calculate their Scrabble scores, and keep track of the total score. You can quit the game at any time by typing "quit."

## Running Tests
To ensure the correctness of the functionalities, run the unit tests using:
```
python -m unittest discover

```
This will execute all test cases defined in test_scrabble.py.