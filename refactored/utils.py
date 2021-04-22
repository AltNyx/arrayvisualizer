from __future__ import annotations
from tkinter import Canvas
from tkinter import Tk
import time


class Box:
    ''' Creates a rectangle object

    param x: x coord of bottom left of the rectangle
    param y: y coord of bottom left of the rectange
    param val: value of the box
    param box: a rectangle box object in canvas
    param text: a text object in canvas
    '''

    def __init__(self, x: int, y: int, val: int, box, text):
        self.x = x
        self.y = y
        self.val = val
        self.box = box
        self.text = text

    def __lt__(self, other: Box):
        return self.val < other.val

    def __gt__(self, other: Box):
        return self.val > other.val

    def __eq__(self, other: Box):
        return self.val == other.val


def swap(box1: Box, box2: Box, animation_speed: int, canvas: Canvas, tk: Tk) -> None:
    ''' 
    Swapping the positions of both boxes in canvas
    Assuming box1 is always to the left of box2
    '''
    distance = box2.x - box1.x

    while distance > 0:
        # Move rectangle1 to position of rectangle 2
        canvas.move(box1.box, animation_speed, 0)
        canvas.move(box1.text, animation_speed, 0)

        # Move rectange2 to position of rectangel1
        canvas.move(box2.box, -animation_speed, 0)
        canvas.move(box2.text, -animation_speed, 0)

        # Update canvas
        tk.update()

        distance -= animation_speed
        time.sleep(0.01)

    time.sleep(0.05)

    # Updating the new positions of boxes
    box1.x, box2.x = box2.x, box1.x


def generate_boxes(array: list[int], x: int, y: int, height_factor: int, canvas: Canvas) -> list[Box]:
    '''
    Creates n boxes with random values in canvas
    Returns a list of Boxes
    '''
    boxes = []

    # Font
    font = "none 10 bold"

    for i, num in enumerate(array):
        height = y-num*height_factor
        box = canvas.create_rectangle(x, height, x+22, y)
        text = canvas.create_text(x+10, height-10, text=num, font=font)
        boxes.append(Box(x=x, y=y, val=num, box=box, text=text))
        x += 26

    return boxes
