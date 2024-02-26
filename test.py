import tkinter as tk
import numpy as np

# Create a Tkinter window
window = tk.Tk()
window.title("Move Box with Interpolation and Easing")

# Set window size and disable resizing
window.geometry("800x400")
window.resizable(False, False)

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
canvas = tk.Canvas(window, width=800, height=400, bg="white")
canvas.pack()

# Create the boxes
box_image = tk.PhotoImage(file="assets/box.png")
boxes = [canvas.create_image(100 + i*150, 300, image=box_image) for i in range(5)]

# Store the state of the boxes
box_states = {box: False for box in boxes}  # False means the box is down, True means the box is up
last_moved_box = None

# Animate the box with interpolation and easing when clicked
def on_box_click(event):
    global last_moved_box
    item = canvas.find_withtag("current")[0]
    if box_states[item] == False:  # If the box is down
        if last_moved_box is not None:  # If there is a box that has been moved up
            animate_box(canvas, last_moved_box, canvas.coords(last_moved_box)[1], canvas.coords(last_moved_box)[1] + 200, 500, 50, ease_in_out_quad)
            box_states[last_moved_box] = False
        animate_box(canvas, item, canvas.coords(item)[1], canvas.coords(item)[1] - 200, 500, 50, ease_in_out_quad)
        box_states[item] = True
        last_moved_box = item

for box in boxes:
    canvas.tag_bind(box, "<Button-1>", on_box_click)

# Start the Tkinter event loop
window.mainloop()