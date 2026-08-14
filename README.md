🎯 Number Guessing Game

A simple Number Guessing Game built with Python. The project includes both a command-line version and an interactive Streamlit web version.

🚀 Live Demo

Play the web version online:

👉 Number Guessing Game

📖 Description

In this game, the computer randomly selects a number between 1 and 100, and the player tries to guess the secret number.

After each guess, the game gives a hint:

If the guess is too high, the player is asked to choose a lower number.
If the guess is too low, the player is asked to choose a higher number.
When the correct number is guessed, the player wins.

The player starts with a score of 100, and each incorrect attempt decreases the score by 1 point.

✨ Features
🎲 Random number generation
🔢 Number guessing between 1 and 100
💯 Score system
⬆️ High and low hints
✅ Input validation
🔄 Play again option
❌ Quit option
🌐 Interactive Streamlit web interface
💻 Command-line version
🎮 Game Rules
The computer chooses a random number between 1 and 100.
Enter your guess.
If your guess is too high, try a lower number.
If your guess is too low, try a higher number.
Each incorrect guess reduces your score by 1 point.
Guess the correct number to win.
In the command-line version, enter q to quit.
🛠️ Technologies
Python 3
Streamlit
Random module
📂 Project Structure
Number_guessing_game/
│
├── main.py
├── requirements.txt
├── README.md
│
└── streamlit/
    └── by_streamlit.py
💻 Run the Command-Line Version

Clone the repository:

git clone https://github.com/pashmakiana-cell/Number_guessing_game.git

Go to the project directory:

cd Number_guessing_game

Run the game:

python main.py
🌐 Run the Streamlit Version Locally

Install the required dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run streamlit/by_streamlit.py

The application will open in your web browser.

📸 Example

The game gives hints after each guess and keeps track of the player's score.

Example:

Enter a number between 1 and 100: 50
Enter a bigger number than 50: 75
Enter a lower number than 75: 62

Exactly! You win.
Your score is: 97 / 100
🔮 Future Improvements
Multiple difficulty levels
High score system
Statistics tracking
Limited number of attempts
Improved user interface
More game modes
📄 License

This project is licensed under the MIT License.


👤 Author

Amir Hossein Pashmakian

Email : pashmakiana@gmail.com
LinkedIn: https://www.linkedin.com/in/amirhossein-pashmakian-645909415/
GitHub: https://github.com/pashmakiana-cell
