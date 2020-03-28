from tkinter import *
import time
import random
num = 12

tk = Tk()
tk.title("Animaitons")
HEIGHT = 500
WIDTH = 1000
canvas = Canvas(tk, height = HEIGHT, width = WIDTH)
canvas.pack()

#heading
canvas.create_text(WIDTH / 2, 75, text = "Binary Search", font = "none 25 bold underline italic", fill = "Green2")

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

for i in range(num):
    #index of array
    canvas.create_text(txt_xpos, txt_ypos - 10, text = i, font = "none 10", fill = "Black")
    txt_xpos += 50

#textpos
txt_x1 = WIDTH / 2 - (num / 2 * 50) + 25
txt_y1 = HEIGHT / 2

element_array = []
for i in  range(num):
    element_array.append(random.randrange(0, 50))

element_array.sort()
#storing text object in array(to animate)
values = []

for i in range(num):
    values.append(canvas.create_text(txt_x1, txt_y1, text = element_array[i] , font = "none 20 bold"))
    txt_x1 += 50




#position reset
x1 = (WIDTH / 2) - (num / 2 * 50)
y1 = HEIGHT / 2 - 25
x2 = x1 + 50
y2 = HEIGHT / 2 + 25

#position low
x1_low = x1
y1_low = y1 + 75
x2_low = x2
y2_low = y2 + 75

#position high
x1_high = x1 + 50 * (num - 1)
x2_high = x1_high + 50
y1_high = y1_low
y2_high = y2_low

#position mid
x1_mid = x1 + 50 * ((num - 1) // 2)
x2_mid = x1_mid + 50
y1_mid = y1_low
y2_mid = y2_low




#binary_search logic

position_box = [] #contains low --> high --> mid
text_box = []

low = 0
position_box.append(canvas.create_rectangle(x1_low, y1_low, x2_low, y2_low, fill = "cyan"))
text_box.append(canvas.create_text(x1_low + 25, y1_low + 25, text = "Low", font = "none 10 bold"))

high = num - 1
position_box.append(canvas.create_rectangle(x1_high, y1_high, x2_high, y2_high, fill = "cyan"))
text_box.append(canvas.create_text(x1_high + 25, y1_high + 25, text = "High", font = "none 10 bold"))

mid = (high + low) // 2
position_box.append(canvas.create_rectangle(x1_mid, y1_mid, x2_mid, y2_mid, fill = "cyan"))
text_box.append(canvas.create_text(x1_mid + 25, y1_mid + 25, text = "Mid", font = "none 10 bold"))

key = int(input("Enter key to be searched:"))

#animation speed
xspeed = 1
yspeed = 0

#message_array
message_box = []

while low <= high:
    mid = (high + low) // 2

    if key == element_array[mid]:
        if len(message_box) != 0:
            canvas.delete(message_box[0])
        canvas.create_text(WIDTH / 2, HEIGHT - HEIGHT / 8, text = "Key is found at position %d" %(mid + 1), font = "none 20 italic bold", fill = "lime")
        break
    elif key > element_array[mid]:
        if len(message_box) != 0:
            canvas.delete(message_box[0])
        message_box.append(canvas.create_text(WIDTH / 2, HEIGHT - HEIGHT / 8, text = "Key > Arr[mid]", font = "none 20 italic bold", fill = "lime"))
        while True:
            canvas.move(position_box[0], xspeed, yspeed)
            canvas.move(text_box[0], xspeed, yspeed)
            pos_low = canvas.coords(position_box[0])
            if pos_low[2] == x2_mid + 50:
                break
            tk.update()
            time.sleep(0.01)
        x1_low = pos_low[0]
        x2_mid = (x1_low + x2_high) // 2
        if x2_mid % 50 != 0:
            x2_mid -= 25
        while True:
            canvas.move(position_box[2], xspeed, yspeed)
            canvas.move(text_box[2], xspeed, yspeed)
            pos_mid = canvas.coords(position_box[2])
            if pos_mid[2] == x2_mid:
                break
            tk.update()
            time.sleep(0.01)          
        low = mid + 1
        
    else:
        if len(message_box) != 0:
            canvas.delete(message_box[0])
        message_box.append(canvas.create_text(WIDTH / 2, HEIGHT - HEIGHT / 8, text = "Key < Arr[Mid]", font = "none 20 italic bold", fill = "lime"))
        while True:
            canvas.move(position_box[1], -xspeed, yspeed)
            canvas.move(text_box[1], -xspeed, yspeed)
            pos_high = canvas.coords(position_box[1])
            if pos_high[2] == x2_mid - 50:
                break
            tk.update()
            time.sleep(0.01)
        x2_high = pos_high[2] + 50
        x2_mid = (x1_low + x2_high) // 2
        if x2_mid % 50 != 0:
            x2_mid -= 25
        while True:
            canvas.move(position_box[2], -xspeed, yspeed)
            canvas.move(text_box[2], -xspeed, yspeed)
            pos_mid = canvas.coords(position_box[2])
            if pos_mid[2] == x2_mid:
                break
            tk.update()
            time.sleep(0.01)
        high = mid - 1

if len(message_box) != 0:
    canvas.delete(message_box[0])

if high < low:
    canvas.create_text(WIDTH / 2, HEIGHT - HEIGHT / 8, text = "Key not found", font = "none 20 italic bold", fill = "lime")



# #insertion animation
# ele = int(input("Enter element to be inserted:"))
# pos = int(input("Enter the position of the element:"))


# print(values)
# if pos < 1 or pos > n:
#     print("Invalid position!")
#     canvas = Canvas(tk, height = HEIGHT, width = WIDTH, bg = "cyan")

# else:
#     for i in range(n - 1, pos - 2, -1):
#         #animation speed
#         xspeed = 1
#         yspeed = 0
#         fin_pos = canvas.coords(values[i])
#         while True:
#             canvas.move(values[i], xspeed, yspeed)
#             position = canvas.coords(values[i])
#             if position[0] >= fin_pos[0] + 50:
#                 xspeed = 0
#                 break
#             tk.update()
#             time.sleep(0.01)


#     #txt_pos reset
#     txt_x1 = WIDTH / 2 - (num / 2 * 50) + 25
#     txt_y1 = HEIGHT / 2

#     #1ms delay before inserting
#     tk.update()
#     time.sleep(1)
#     move_ele = canvas.create_text(txt_x1 + 50 * (pos - 1), 100, text = ele, font = "none 20 bold")
    
    
#     while True:
#         canvas.move(move_ele, 0, 1)
#         move_ele_pos = canvas.coords(move_ele)
#         if move_ele_pos[1] >= txt_y1:
#             break
#         tk.update()
#         time.sleep(0.01)

#     #inserted at position text
#     canvas.create_text(WIDTH / 2, txt_y1 + 150, text = "The element %d inserted at position %d" %(ele,pos), font = "none 20 bold italic underline", fill = "Green2")
        
canvas.mainloop()