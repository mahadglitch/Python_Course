import tkinter as tk
import random

# Function to determine the winner
def play(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        result = f"Draw! Both chose {user_choice}"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = f"You Win! Computer chose {computer_choice}"
    else:
        result = f"You Lose! Computer chose {computer_choice}"
    
    result_label.config(text=result)

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

# Heading
heading = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20))
heading.pack(pady=20)

# Buttons for user choice
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play('Rock'))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play('Paper'))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play('Scissors'))
scissors_button.grid(row=0, column=2, padx=5)

# Label to show result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Run the window
root.mainloop()
