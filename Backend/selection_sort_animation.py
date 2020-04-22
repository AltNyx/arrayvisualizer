from tkinter import *
import time
import random
import timeit
n = 20

tk = Tk()
tk.title("Selection Sort")

#(make height and width dynamic)
HEIGHT = 500
WIDTH = 1000
canvas = Canvas(tk, height = HEIGHT, width = WIDTH)
canvas.pack()

#initial position

x1 = WIDTH // 2 - n // 2 * 24
x2 = x1 + 21

y1 = HEIGHT // 2 + HEIGHT // 4
y2 = y1

#sample_array (might make it random using random function)
new_arr = []
for i in range(n):
    new_arr.append(random.randrange(1,50))
#new_arr = [25, 34, 18, 21, 13, 5, 15, 7, 9, 10, 16, 15, 13, 19, 34, 9, 4, 3, 2, 7]

nums = new_arr.copy()
#EXECUTION TIME
SETUP = '''
from selection_sort_algorithm import selection_sort
from __main__ import nums
'''
CODE = '''
sorted_arr = selection_sort(nums, len(nums))
'''
execution_time = timeit.timeit(setup=SETUP, stmt=CODE, number=1000)  #time of 1000 executions in seconds
sorting_time = "%.5f ms" %(execution_time)

#execution time display
h_pos = WIDTH - 100
y_pos = 50
canvas.create_text(h_pos, y_pos, text="Sorting time\n{}".format(sorting_time), font = "none 12 bold", fill="#254bed")

#empty array to store individual box and text so that they could be animated
boxes = []
texts = []

#color
initial_color = "#254bed"
comp_color = "#ff0036"
pass_color = "#00ffb4"

#height of each bar
bar_height = (HEIGHT // 2) // max(new_arr) #inbuilt func to find max element in an array

#HEADING
canvas.create_text(WIDTH // 2, 50, text = "SELECTION SORTING", font = "none 25 italic underline bold", fill = initial_color)

#unsorted elements
for i in range(0, len(new_arr)):
    boxes.append(canvas.create_rectangle(x1, y1 - bar_height * new_arr[i], x2, y2, fill = initial_color))
    texts.append(canvas.create_text(x1 + 10, y1 - 10 - bar_height * new_arr[i], text = new_arr[i], font = "none 10 bold"))
    x1 += 24
    x2 += 24

#Sorting animation speed
x_animation_speed = 2
y_animation_speed = 0

#1ms delay so that sorting doesn't take place instantly
tk.update()
time.sleep(1)

#selection_sort sorting algorithm
for i in range(n - 1):
    pos = i
    canvas.itemconfig(boxes[pos], fill = comp_color)
    tk.update()
    time.sleep(0.5)

    for j in range(i + 1, n): 
        #canvas.itemconfig(boxes[j], fill = "Purple")
        if new_arr[j] < new_arr[pos]:
            temp = pos
            pos = j
            canvas.itemconfig(boxes[pos], fill = comp_color)
            canvas.itemconfig(boxes[temp], fill = initial_color)

            #0.5ms delay after each updated value of pos
            tk.update()
            time.sleep(0.5)

    
     


    pos_box1 = canvas.coords(boxes[i])                
    left_box = pos_box1[0]


    while True:
        #move larger element
        canvas.move(boxes[i], x_animation_speed, y_animation_speed)
        canvas.move(texts[i], x_animation_speed, y_animation_speed)
        #move smaller element
        canvas.move(boxes[pos], - x_animation_speed, y_animation_speed)
        canvas.move(texts[pos], - x_animation_speed, y_animation_speed)


        #get real time position of any1 box
        pos_box2 = canvas.coords(boxes[pos])


        #when the position of the box is equal to the position of the box to be swapped, break
        if pos_box2[0] <= left_box:
            new_arr[pos], new_arr[i] = new_arr[i], new_arr[pos]
            boxes[pos], boxes[i] = boxes[i], boxes[pos]
            texts[pos], texts[i] = texts[i], texts[pos]
            break


        tk.update()
        time.sleep(0.005)
    canvas.itemconfig(boxes[i], fill = pass_color)
canvas.itemconfig(boxes[- 1], fill = pass_color)


canvas.mainloop()