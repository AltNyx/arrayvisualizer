from tkinter import *
import time
num = 10
n = int(input("Enter num of elements:"))

tk = Tk()
tk.title("Animaitons")
HEIGHT = 500
WIDTH = 700
canvas = Canvas(tk, height = HEIGHT, width = WIDTH)
canvas.pack()

#heading
canvas.create_text(WIDTH / 2, 75, text = "INSERT ELEMENT", font = "none 25 bold underline italic", fill = "Green2")

#position of base rectangle
x1 = (WIDTH / 2) - (num / 2 * 50)
y1 = HEIGHT / 2 - 25
x2 = x1 + 50
y2 = HEIGHT / 2 + 25


#name of array
canvas.create_text(x1 - 30, y1 + 25, text = "Arr", font = "none 20 bold", fill = "Black")


for i in range(0, num):
    canvas.create_rectangle(x1, y1, x2, y2, fill = "Green2")
    x1 += 50
    x2 += 50

#position of txt
txt_xpos = WIDTH / 2 - (num / 2 * 50) + 25 
txt_ypos = HEIGHT / 2 - 25

for i in range(0, num):
    #base address of array
    address = 1000 + (4 * i) #say size of int = 4
    canvas.create_text(txt_xpos, txt_ypos + 60, text = address, font = "none 10", fill = "Black")
    #index of array
    canvas.create_text(txt_xpos, txt_ypos - 10, text = i, font = "none 10", fill = "Black")
    txt_xpos += 50

#textpos
txt_x1 = WIDTH / 2 - (num / 2 * 50) + 25
txt_y1 = HEIGHT / 2

#storing text object in array(to animate)
values = []

for i in range(n):
    values.append(canvas.create_text(txt_x1, txt_y1, text = input("Enter element:"), font = "none 20 bold"))
    txt_x1 += 50


#insertion animation
ele = int(input("Enter element to be inserted:"))
pos = int(input("Enter the position of the element:"))


print(values)
if pos < 1 or pos > n:
    print("Invalid position!")
    canvas = Canvas(tk, height = HEIGHT, width = WIDTH, bg = "cyan")

else:
    for i in range(n - 1, pos - 2, -1):
        #animation speed
        xspeed = 1
        yspeed = 0
        fin_pos = canvas.coords(values[i])
        while True:
            canvas.move(values[i], xspeed, yspeed)
            position = canvas.coords(values[i])
            if position[0] >= fin_pos[0] + 50:
                xspeed = 0
                break
            tk.update()
            time.sleep(0.01)


    #txt_pos reset
    txt_x1 = WIDTH / 2 - (num / 2 * 50) + 25
    txt_y1 = HEIGHT / 2

    #1ms delay before inserting
    tk.update()
    time.sleep(1)
    move_ele = canvas.create_text(txt_x1 + 50 * (pos - 1), 100, text = ele, font = "none 20 bold")
    
    
    while True:
        canvas.move(move_ele, 0, 1)
        move_ele_pos = canvas.coords(move_ele)
        if move_ele_pos[1] >= txt_y1:
            break
        tk.update()
        time.sleep(0.01)

    #inserted at position text
    canvas.create_text(WIDTH / 2, txt_y1 + 150, text = "The element %d inserted at position %d" %(ele,pos), font = "none 20 bold italic underline", fill = "Green2")
        
canvas.mainloop()