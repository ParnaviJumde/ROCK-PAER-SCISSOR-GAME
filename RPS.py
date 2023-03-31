import random
import PySimpleGUI as sg

def play_game():
    valid_choices = ("rock", "paper", "scissors")

    # Define GUI layout
    layout = [
        [sg.Text("Choose your weapon: ")],
        [sg.Radio("Rock", "weapon", key="rock"), sg.Radio("Paper", "weapon", key="paper"), sg.Radio("Scissors", "weapon", key="scissors")],
        [sg.Button("Play"), sg.Button("Quit")],
        [sg.Text("", key="result")]
    ]
    window = sg.Window("Rock Paper Scissors", layout)

    while True:
        event, values = window.read()
        if event in (None, "Quit"):
            break

        key_of_true_value = next(key for key, value in values.items() if value)
        player = key_of_true_value
        computer = random.choice(valid_choices)
        print( key_of_true_value + " vs " + computer )
        result_text = ""

        win_conditions = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        if player == computer:
            result_text = "It's a tie!"
        elif win_conditions[player] == computer:
            result_text = "You win!"
        else:
            result_text = "You lose!"

        window["result"].update(result_text)

    window.close()

if __name__ == "__main__":
    play_game()
