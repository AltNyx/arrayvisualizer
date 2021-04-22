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


def bubble_sort(boxes):
    initial_color = "#2299AB"
    comparision_color = "#8D00FF"
    final_color = "#00FFCE"
    animation_speed = 1

    # Set all boxes color to initial color
    for box in boxes:
        set_color(box, initial_color, canvas)

    n = len(boxes)
    for i in range(n-1):
        for j in range(n-i-1):
            if boxes[j] > boxes[j+1]:
                set_color(boxes[j], comparision_color, canvas)
                set_color(boxes[j+1], comparision_color, canvas)

                swap(boxes[j], boxes[j+1], animation_speed, canvas, tk)
                boxes[j], boxes[j+1] = boxes[j+1], boxes[j]

                time.sleep(0.1)

                set_color(boxes[j], initial_color, canvas)
                set_color(boxes[j+1], initial_color, canvas)

        set_color(boxes[j+1], final_color, canvas)

    set_color(boxes[0], final_color, canvas)


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
bubble_sort(boxes)
canvas.mainloop()
