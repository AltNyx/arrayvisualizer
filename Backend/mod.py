from tkinter import *
import time
n = int(input("Enter num of elements:"))

tk = Tk()
tk.title("Animaitons")
HEIGHT = 2000
WIDTH = 2000
canvas = Canvas(tk, height = HEIGHT, width = WIDTH)

canvas.pack()

#position of base rectangle
x1 = 100
y1 = 200
x2 = 150
y2 = 250

#class for arraybox object
class ArrayBox:
    def __init__(self, pos_x1, pos_y1, pos_x2, pos_y2 , color):
        self.color = color
        self.element = canvas.create_rectangle(pos_x1, pos_y1, pos_x2, pos_y2, fill = self.color)

#class for text object
class Text:
    def __init__(self, pos_x1, pos_y1, text_value, font_char, color):
        self.color = color
        self.element = canvas.create_text(pos_x1, pos_y1, text = text_value, font = font_char, fill = self.color)
        #speed of text
        self.xspeed = 0
        self.yspeed = 1.5
        #font_char format --> font = "font_name font_size bold/underline"


    #function to animate text
    def animate_text(self):
        canvas.move(self.element, self.xspeed, self.yspeed)
        pos = canvas.coords(self.element) #position of the element (coordinates)
        
        if pos[1] >= y1 + 25:   #y1 + 25 = 225(till element reaches inside the box)
            self.yspeed = 0

#name of array
array_name = Text(x1 - 30, y1 + 25, "Arr", "none 20 bold", "Black")

for i in range(0, n):
    arrayBox = ArrayBox(x1, y1, x2, y2, "#80CBC4")
    
    x1 += 50
    x2 += 50

    
##########
#Test Code
#mybox = canvas.create_rectangle(10, 10, 50, 50, fill = "Black")
#canvas.itemconfig(mybox, fill = "Green2")
##########


#starting position of elements
right = 125
top = 100

#arr = []
#for i in range(0, n):
    #arr.append(input("Enter element:"))

for i in range(0, n):
    array_elements = Text(right, top, input("Enter element:"), "none 20 bold", "Black")
    
    while True:
        array_elements.animate_text()
        if array_elements.yspeed == 0:
            break
        tk.update()
        time.sleep(0.01)
    right += 50

#position of txt
txt_xpos = 125 
txt_ypos = 200

for i in range(0, n):
    #base address of array
    address = 1000 + (4 * i) #say size of int = 4
    address_text = Text(txt_xpos, txt_ypos + 60, address, "none 10", "Black")
    #index of array
    index_text = Text(txt_xpos, y1 - 10, i, "none 10", "Black")
    txt_xpos += 50



canvas.mainloop()