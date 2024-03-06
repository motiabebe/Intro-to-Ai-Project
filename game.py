import tkinter as tk
import numpy as np
import random
from tkinter import messagebox


# Create a Tkinter window
window = tk.Tk()
window.title("Move Box with Interpolation and Easing")

# Set window size and disable resizing
window.geometry("1080x720")
window.resizable(False, False)

# At the beginning of your script

# Interpolation function with easing
def interpolate_with_easing(start, end, steps, easing_func):
    t = np.linspace(0, 1, steps)
    interpolated_values = [(end - start) * easing_func(x) + start for x in t]
    return interpolated_values

# Easing function
def ease_in_out_quad(x):
    if x < 0.5:
        return 2 * x ** 2
    else:
        return 1 - 2 * (1 - x) ** 2

# Function to animate box with interpolation and easing
def animate_box(canvas, item, start_y, end_y, duration, steps, easing_func):
    for y in interpolate_with_easing(start_y, end_y, steps, easing_func):
        canvas.move(item, 0, y - canvas.coords(item)[1])
        canvas.update()
        canvas.after(duration // steps)

# Create a canvas to place the box



from PIL import Image, ImageTk

# Load the background image and resize it
image = Image.open("assets/Bg.png")
image = image.resize((1080, 720), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image)

# Create a canvas to place the box
canvas = tk.Canvas(window, width=1080, height=720, bg="white")
canvas.pack()

# Add the background image to the canvas
canvas.create_image(0, 0, image=background_image, anchor='nw')

# ... rest of your code ...








from PIL import Image, ImageTk
import tkinter as tk

# Global list to hold the image objects and the items
# Global list to hold the image objects and the items
global_images = []
items = []

def create_images():
    global items  # Declare items as global at the beginning of the function
    # Load the images and resize them
    image_files = ["Chair 2.png", "Chair 1.png", "Tv.png", "Couch.png" ,"Thing.png" ]
    for image_file in image_files:
        image = Image.open(f"assets/{image_file}")
        width, height = image.size
        image = image.resize((int(width * 0.5), int(height * 0.5)), Image.LANCZOS)
        global_images.append(ImageTk.PhotoImage(image))

    # Manually specify the x and y coordinates for each object
    items.append(canvas.create_image(100+60, 720-20, image=global_images[0], anchor='s'))  
    items.append(canvas.create_image(300+60, 720-20, image=global_images[1], anchor='s'))  
    items.append(canvas.create_image(500+60, 720-20, image=global_images[2], anchor='s'))  
    items.append(canvas.create_image(700+60, 720-20, image=global_images[3], anchor='s'))  
    items.append(canvas.create_image(900+60, 720-20, image=global_images[4], anchor='s'))  



# Call the functions
create_images()
# create_canvas()

# Store the initial coordinates of the items
initial_coordinates = {item: canvas.coords(item) for item in items}


# Create the hidden images



empty = tk.PhotoImage(file="assets/empty.png")
found = tk.PhotoImage(file="assets/found.png")

# Manually specify the x and y coordinates for each hidden image
hidden_images = []
hidden_images.append(canvas.create_image(100+40, 720-20-30, image=empty, anchor='s'))  
hidden_images.append(canvas.create_image(300+60, 720-20-50, image=empty, anchor='s'))  
hidden_images.append(canvas.create_image(500+60, 720-20, image=empty, anchor='s'))     
hidden_images.append(canvas.create_image(700+60, 720-20-20, image=empty, anchor='s'))  
hidden_images.append(canvas.create_image(900+60, 720-20+20, image=empty, anchor='s'))  

hidden_image = random.choice(hidden_images)
canvas.itemconfig(hidden_image, image=found)

# Move the hidden images behind the items
for item, hidden_image in zip(items, hidden_images):
    canvas.tag_lower(hidden_image, item)






from tkinter import Label
# Initialize the score
score = 0

# Create a label to display the score
score_label = Label(window, text=f"Score: {score}", font=("Helvetica", 30))
score_label.place(x=0, y=0)  # Place the label in the top left corner









# Store the state of the items
item_states = {item: False for item in items}  # False means the item is down, True means the item is up
last_moved_item = None
trials = 2

# Animate the box with interpolation and easing when clicked
# Create a dictionary mapping the hidden images to their associated items
hidden_image_items = {hidden_image: item for hidden_image, item in zip(hidden_images, items)}

# ...

def on_item_click(event):
    global last_moved_box
    global trials
    global score 

    last_moved_box = None
    item = canvas.find_withtag("current")[0]
    if item_states[item] == False:  # If the box is down
        if last_moved_box is not None:  # If there is a box that has been moved up
            animate_box(canvas, last_moved_box, canvas.coords(last_moved_box)[1], canvas.coords(last_moved_box)[1] + 200, 500, 50, ease_in_out_quad)
            item_states[last_moved_box] = False
        animate_box(canvas, item, canvas.coords(item)[1], canvas.coords(item)[1] - 200, 500, 50, ease_in_out_quad)
        item_states[item] = True
        last_moved_box = item
        if item == hidden_image_items[hidden_image]:  # Check if the clicked item is associated with the hidden image
            messagebox.showinfo("Congratulations!", "You found the hidden image!")
            score += 1
            score_label['text'] = f"Score: {score}"  # Update the score label
            restart_game()
        else:
            trials -= 1
            if trials == 0:
                messagebox.showinfo("Game Over", "You failed to find the hidden image. The game will restart.")
                restart_game()







def restart_game():
    global trials, hidden_image, score
    trials = 2
    score_label['text'] = f"Score: {score}"  # Update the score label
    for box in items:
        # Reset the item's coordinates to its initial coordinates
        x, y = initial_coordinates[box]
        canvas.coords(box, x, y)
        item_states[box] = False
    for image in hidden_images:
        canvas.itemconfig(image, image=empty)
    hidden_image = random.choice(hidden_images)
    canvas.itemconfig(hidden_image, image=found)




for box in items:
    canvas.tag_bind(box, "<Button-1>", on_item_click)

# Start the Tkinter event loop
window.mainloop()