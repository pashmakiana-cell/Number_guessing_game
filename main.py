
import random
 
 
def play_game():
    """
    Run a single session of the Number Guessing Game.
 
    The computer randomly picks a number between 1 and 100.
    The player keeps guessing until they either guess the
    correct number, or type 'q' to quit.
 
    Score starts at 100 and decreases by 1 for every guess made.
    """
    score = 100
    computer_number = random.randint(1, 100)
 
    user_input = input("Enter a number between 1 and 100 (or 'q' to quit): ")
 
    while True:
        score -= 1
 
        # Quit the game
        if user_input == 'q':
            print("Thank you for playing!")
            break
 
        # Validate that the input is a number
        if not user_input.isdigit():
            user_input = input(
                f"'{user_input}' is invalid input. Please try again. "
                "Enter a number between 1 and 100 (or 'q' to quit): "
            )
            continue
 
        user_number = int(user_input)
 
        # Validate the number range
        if user_number < 1 or user_number > 100:
            user_input = input(
                f"'{user_number}' is out of range. Please try again. "
                "Enter a number between 1 and 100 (or 'q' to quit): "
            )
            continue
 
        # Compare the guess with the computer's number
        if user_number > computer_number:
            user_input = input(f"Try a lower number than {user_number}: ")
            continue
 
        if user_number < computer_number:
            user_input = input(f"Try a higher number than {user_number}: ")
            continue
 
        # user_number == computer_number -> player wins
        print(f"Exactly! You win! Your score is: {score} / 100")
        break
 
 
def ask_play_again():
    """
    Ask the player whether they want to start a new game.
 
    Returns:
        str: The user's answer ('Y' or 'N', case-sensitive as entered).
    """
    return input("Do you want to play again? (Y/N): ").strip()
 
 
# ---------- Main Program ----------
 
play_game()
 
while ask_play_again() == 'Y':
    play_game()
 
print("Goodbye!")
 

 
 

