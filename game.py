import tkinter as tk
import random

# Constants
NUM_BOXES = 10
NUM_ITEMS = 5
NUM_GUESSES = 5

# Create boxes and items
boxes = [0]*NUM_BOXES
items = random.sample(range(NUM_BOXES), NUM_ITEMS)

# Assign items to boxes
for item in items:
    boxes[item] = 1

# Create a Tkinter window
window = tk.Tk()
window.title("Hide and Seek Game")

# Set window size and disable resizing
window.geometry("600x400")  # adjust as needed
window.resizable(False, False)

# Load images
box_image = tk.PhotoImage(file="box.png")  # replace with your image file
found_image = tk.PhotoImage(file="found.png")  # replace with your image file
empty_image = tk.PhotoImage(file="empty.png")  # replace with your image file

# Create a label to display the game status
status_label = tk.Label(window, text=f"You have {NUM_GUESSES} guesses to find all the hidden items!", font=('Helvetica', 14))
status_label.grid(row=0, column=0, columnspan=NUM_BOXES//2, pady=10)

# Create buttons for each box
buttons = []
for i in range(NUM_BOXES):
    button = tk.Button(window, image=box_image, command=lambda i=i: check_box(i))
    button.grid(row=(i//2)+1, column=i%2, padx=5, pady=5)
    buttons.append(button)

# Counter for guesses
guesses = NUM_GUESSES

# Function to handle button clicks
def check_box(i):
    global guesses
    guesses -= 1
    if boxes[i] == 1:
        buttons[i].config(image=found_image, state="disabled")
        boxes[i] = 0
        if sum(boxes) == 0:
            status_label.config(text="Congratulations, you found all items!")
    else:
        buttons[i].config(image=empty_image, state="disabled")
    if guesses == 0 and sum(boxes) > 0:
        for i in range(NUM_BOXES):
            buttons[i].config(state="disabled")
        status_label.config(text="Game over! You didn't find all items.")

# Start the Tkinter event loop
window.mainloop()