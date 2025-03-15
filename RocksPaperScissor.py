import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Set the window size to 300x300
root.geometry("300x300")
# Options
choices = ["Rock", "Paper", "Scissors"]

# Function to determine the winner
def determine_winner(player_choice):
    computer_choice = random.choice(choices)
    
    # Update the labels
    player_label.config(text=f"Player: {player_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")
    
    # Determine the winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Scissors" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    # Update the result label
    result_label.config(text=result)

# Create the labels
player_label = tk.Label(root, text="Player: ", font=("Arial", 14))
player_label.pack()

computer_label = tk.Label(root, text="Computer: ", font=("Arial", 14))
computer_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 16), fg="blue")
result_label.pack()

# Buttons for choices
for choice in choices:
    button = tk.Button(root, text=choice, font=("Arial", 14), 
                       command=lambda c=choice: determine_winner(c))
    button.pack(pady=5)

# Run the GUI loop
root.mainloop()
