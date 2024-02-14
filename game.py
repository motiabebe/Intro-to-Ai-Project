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
window.geometry("1280x720")
window.resizable(False, False)

# Load images
box_image = tk.PhotoImage(file="assets/box.png")  
found_image = tk.PhotoImage(file="assets/found.png")  
empty_image = tk.PhotoImage(file="assets/empty.png")  

# Create a label to display the game status
status_label = tk.Label(window, text=f"You have {NUM_GUESSES} guesses to find all the hidden items!", font=('Helvetica', 14))
status_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Create buttons for each box
buttons = []
for i in range(NUM_BOXES):
    button = tk.Button(window, image=box_image, command=lambda i=i: check_box(i))
    button.grid(row=i//2+1, column=i%2, padx=5, pady=5)
    buttons.append(button)

# Counter for guesses
guesses = NUM_GUESSES


# At the start of the function, the guesses counter is decremented by 1, 
#  that the player has used one guess.

# The function then checks if the box at index i contains an item 
# (i.e., if boxes[i] is 1). If it does, the function updates the corresponding 
# button to display the found_image and disables it to prevent further interaction. 
# It also sets boxes[i] to 0 to indicate that the item has been found. 
# If all items have been found (i.e., if the sum of boxes is 0), 
# it updates the status_label to congratulate the player.

# If the box does not contain an item, the function updates the button to 
# display the empty_image and disables it.

# Finally, if the player has used all their guesses and there are still items 
# left to find (i.e., if guesses is 0 and the sum of boxes is greater than 0), 
# the function disables all the buttons and updates the status_label to indicate 
# that the game is over and the player did not find all the items.
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