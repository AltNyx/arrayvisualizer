import random
import time
from tkinter import *
import timeit

n = 20

tk = Tk()
tk.title("Bubble Sort")

#(make height and width dynamic)
HEIGHT = 500
WIDTH = 1000
canvas = Canvas(tk, height = HEIGHT, width = WIDTH)
canvas.pack()

#initial position

x1 = WIDTH / 2 - n / 2 * 25
x2 = x1 + 22

y1 = HEIGHT / 2 + HEIGHT / 4
y2 = y1

#sample_array (might make it random using random function)
new_arr = []
for i in range(n):
    new_arr.append(random.randrange(1,50))
#new_arr = [25, 34, 18, 21, 13, 5, 15, 7, 9, 10, 16, 15, 13, 19, 34, 9, 4, 3, 2, 7]

nums = new_arr.copy()
#EXECUTION TIME
SETUP = '''
from bubble_sort import bubble_sort
from __main__ import nums
'''
CODE = '''
sorted_arr = bubble_sort(nums, len(nums))
'''
execution_time = timeit.timeit(setup=SETUP, stmt=CODE, number=1000)  #time of 1000 executions in seconds
sorting_time = "%.5f ms" %(execution_time)

#execution time display
h_pos = WIDTH - 100
y_pos = 50
canvas.create_text(h_pos, y_pos, text="Sorting time\n{}".format(sorting_time), font = "none 12 bold", fill="#2299ab")

#empty array to store individual box and text so that they could be animated
boxes = []
texts = []

#color
initial_color = "#2299ab"
comp_color = "#8d00ff"
pass_color = "#00ffce"

#height of each bar
bar_height = (HEIGHT / 2) / max(new_arr) #inbuilt func to find max element in an array

#HEADING
canvas.create_text(WIDTH / 2, 50, text = "BUBBLE SORTING", font = "none 25 italic underline bold", fill = initial_color)

#unsorted elements
for i in range(0, len(new_arr)):
    boxes.append(canvas.create_rectangle(x1, y1 - bar_height * new_arr[i], x2, y2, fill = initial_color))
    texts.append(canvas.create_text(x1 + 10, y1 - 10 - bar_height * new_arr[i], text = new_arr[i], font = "none 10 bold"))
    x1 += 25
    x2 += 25

#Sorting animation speed
x_animation_speed = 1
y_animation_speed = 0

#1s delay so that sorting does'nt take place instantly
tk.update()
time.sleep(1)

#bubble_sort logic/algorithm
for i in range(n):
    for j in range(0, n - i - 1):
        tk.update()
        time.sleep(0.01) 
        canvas.itemconfig(boxes[j], fill = comp_color)        #changing color when its being compared
        canvas.itemconfig(boxes[j + 1], fill = comp_color)
        
           
        if new_arr[j] > new_arr[j + 1]:
            pos_box1 = canvas.coords(boxes[j])                #getting coordinates of any one box
            left_box = pos_box1[0]

            #0.05s delay before swapping
            tk.update()
            time.sleep(0.05)
            
            while True:
                #move larger element
                canvas.move(boxes[j], x_animation_speed, y_animation_speed)
                canvas.move(texts[j], x_animation_speed, y_animation_speed)
                #move smaller element
                canvas.move(boxes[j + 1], - x_animation_speed, y_animation_speed)
                canvas.move(texts[j + 1], - x_animation_speed, y_animation_speed)
                #get real time position of any1 box
                pos_box2 = canvas.coords(boxes[j + 1])
                #when the position of the box is equal to the position of the box to be swapped, break
                if pos_box2[0] <= left_box:
                    canvas.itemconfig(boxes[j + 1], fill = initial_color)        #changing color to initial color since the second element is smaller 
                    new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
                    boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
                    texts[j], texts[j + 1] = texts[j + 1], texts[j]
                    break
                tk.update()
                time.sleep(0.01)
        else:
            canvas.itemconfig(boxes[j], fill = initial_color)        #changing color of smaller element to initial color
    canvas.itemconfig(boxes[- (1 + i)], fill = pass_color)              #changing color to green since its sorted and is in its final position
    #end of one pass
                
canvas.mainloop()
