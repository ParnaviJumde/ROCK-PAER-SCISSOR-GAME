import random  # Import the random module to generate a random choice for the computer
import PySimpleGUI as sg  # Import the PySimpleGUI module for the graphical user interface

def play_game():
    valid_choices = ("rock", "paper", "scissors")  # Create a tuple of valid choices

    # Define GUI layout
    layout = [
        [sg.Text("Choose your weapon: ")],
        [sg.Radio("Rock", "weapon", key="rock"), sg.Radio("Paper", "weapon", key="paper"), sg.Radio("Scissors", "weapon", key="scissors")],  # Create radio buttons for user to select a weapon
        [sg.Button("Play"), sg.Button("Quit")],  # Create buttons for user to play or quit the game
        [sg.Text("", key="result")]  # Create a text field to display the game result
    ]
    window = sg.Window("Rock Paper Scissors", layout)  # Create a window with the layout

    while True:  # Start a loop for the game
        event, values = window.read()  # Read user events and values from the window
        if event in (None, "Quit"):  # If user clicks the 'X' or 'Quit' button, break the loop and exit the game
            break

        key_of_true_value = next(key for key, value in values.items() if value)  # Get the key of the selected weapon
        player = key_of_true_value  # Assign the selected weapon to the 'player' variable
        computer = random.choice(valid_choices)  # Generate a random choice for the computer
        print( key_of_true_value + " vs " + computer )  # Print the selected weapon and the computer's choice
        result_text = ""  # Initialize the game result text variable

        win_conditions = {  # Create a dictionary of win conditions for the game
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        if player == computer:  # If player and computer select the same weapon, the game is a tie
            result_text = "It's a tie!"
        elif win_conditions[player] == computer:  # If player wins, set the result text to "You win!"
            result_text = "You win!"
        else:  # If player loses, set the result text to "You lose!"
            result_text = "You lose!"

        window["result"].update(result_text)  # Update the game result text in the window

    window.close()  # Close the game window

if __name__ == "__main__":  # If the script is being run as the main program
    play_game()  # Call the 'play_game()' function to start the game
