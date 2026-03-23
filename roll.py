import tkinter as tk
import random

# Dice art dictionary
dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"
    )
}

# Function to roll dice
def roll_dice():
    try:
        num_rolls = int(entry.get())
    except ValueError:
        result_label.config(text="Please enter a number")
        return
    
    output = ""
    for i in range(num_rolls):
        dice_roll = random.randint(1, 6)
        output += "\n".join(dice_art[dice_roll]) + "\n"
        output += f"Dice rolled {i+1} time(s)\n\n"
    
    result_label.config(text=output)

# Tkinter setup
root = tk.Tk()
root.title("🎲 Dice Roller")
root.geometry("400x500")

title = tk.Label(root, text="--- Dice Roller ---", font=("Courier", 16, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

prompt = tk.Label(frame, text="How many times to roll:")
prompt.pack(side=tk.LEFT)

entry = tk.Entry(frame, width=5)
entry.pack(side=tk.LEFT, padx=5)

roll_button = tk.Button(root, text="Roll 🎲", command=roll_dice, bg="lightblue")
roll_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Courier", 12), justify="left")
result_label.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit, bg="tomato")
exit_button.pack(pady=10)

root.mainloop()
