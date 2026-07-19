# Number Guesser Game

## Description

Number Guesser is a simple command-line game written in Python.

The computer randomly selects a number between 1 and 100, and the player tries to guess it. After each guess, the game provides a hint to help the player find the correct number.

The player starts with a score of 100. Each guess decreases the score by 1 point. The game ends when the player guesses the correct number or chooses to quit.

## Features

* Random number generation
* Score system
* Input validation
* High and low hints
* Quit option
* Play again option

## Game Rules

1. Enter a number between 1 and 100.
2. If your guess is too high, the game asks for a lower number.
3. If your guess is too low, the game asks for a bigger number.
4. Each attempt reduces your score by 1.
5. Enter `q` to quit the game.
6. Guess the correct number to win.

## Requirements

* Python 3.x

## How to Run

1. Save the code in a file named `number_guesser.py`.
2. Open a terminal in the project folder.
3. Run the following command:

```bash
python number_guesser.py
```

## Example

```text
enter number between 1 , 100 (for quit enter q )50
enter biger number than 50 : 75
enter a lower number than 75 : 62
exactly you win your score is : 97 / 100
```

## Future Improvements

* Multiple difficulty levels
* High score system
* Statistics tracking
* Limited number of attempts
* Graphical user interface (GUI)

## Licence

This project is licensed under the MIT License.

## How to Contribute

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Submit a pull request.

## Credits

Created as a Python learning project using:

* Functions
* Loops
* Conditions
* User Input Validation
* Random Module

## Contact

For suggestions or bug reports, please open an issue in the repository.
