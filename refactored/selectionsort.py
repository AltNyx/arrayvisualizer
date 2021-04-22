from utils import swap, generate_boxes, Box
from tkinter import Tk, Canvas
import random
import time


tk = Tk()
tk.title('Bubble Sort')

# Canvas
HEIGHT, WIDTH = 500, 1000
canvas = Canvas(tk, height=HEIGHT, width=WIDTH)
canvas.pack()


def set_color(box: Box, color: str, canvas: Canvas) -> None:
    '''Cahnge the color of the box'''
    canvas.itemconfig(box.box, fill=color)
    tk.update()


def selection_sort(boxes):
    initial_color = "#254bed"
    comparision_color = "#ff0036"
    final_color = "#00ffb4"
    animation_speed = 2

    # Set all boxes color to initial color
    for box in boxes:
        set_color(box, initial_color, canvas)

    n = len(boxes)
    for i in range(n):
        min_idx = i
        set_color(boxes[min_idx], comparision_color, canvas)
        for j in range(i+1, n):
            if boxes[min_idx] > boxes[j]:
                set_color(boxes[min_idx], initial_color, canvas)
                min_idx = j
                set_color(boxes[j], comparision_color, canvas)
                time.sleep(0.5)

        swap(boxes[i], boxes[min_idx], animation_speed, canvas, tk)
        boxes[i], boxes[min_idx] = boxes[min_idx], boxes[i]
        set_color(boxes[i], final_color, canvas)


# Array
n = random.randint(10, 30)
array = [random.randint(0, 100) for _ in range(n)]

# Height factor of rectangle
# This is to make sure the height of the rectangle fits in screen
HEIGHT_FACTOR = HEIGHT / 2 / max(array)


# Initial position of the first rectangle
x_initial = (WIDTH/2) - (n/2 * 26)
x_initial += int(x_initial % 2)  # Make x even if x is odd
y_initial = 3/4 * HEIGHT


boxes = generate_boxes(array, x_initial, y_initial, HEIGHT_FACTOR, canvas)
selection_sort(boxes)
canvas.mainloop()
