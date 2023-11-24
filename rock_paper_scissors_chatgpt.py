import random
import tkinter as tk
from tkinter import messagebox

def get_user_choice():
    choice = user_choice.get().lower()
    if choice in {'rock', 'paper', 'scissor'}:
        return choice
    else:
        # Show a pop-up message for an invalid choice
        messagebox.showinfo("Invalid Choice", "Please choose 'rock', 'paper', or 'scissor'.")

def determine_winner(player, pc):
    if player == pc:
        return "It's a tie"
    elif (player == 'rock' and pc == 'scissor') or (player == 'paper' and pc == 'rock') or (player == 'scissor' and pc == 'paper'):
        return "You won"
    else:
        return "You lose / PC won"

def play_game(event=None):
    player_choice = get_user_choice()
    pc_choice = random.choice(['rock', 'paper', 'scissor'])

    result = determine_winner(player_choice, pc_choice)
    messagebox.showinfo("Result", f"Player played: {player_choice}\nPC played: {pc_choice}\nResult: {result}")
    
# Make the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Add a label to instruct the user
label = tk.Label(root, text="Choose your move:", font=("Arial", 14))
label.pack(pady=10)

# Add an entry for the user to input their choice
user_choice = tk.Entry(root , width=20, font=("Arial", 12))
user_choice.pack(pady=10)

# Add a button to trigger the game
play_button = tk.Button(root, text="Play Game", command=play_game, font=("Arial", 12))
play_button.pack(pady=10)

# Bind the <Return> key to the play_game function
root.bind('<Return>', play_game)

# Start the Tkinter event loop
root.mainloop()

