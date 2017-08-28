from Tkinter import *
import thread
import random

root = Tk()
cv = Canvas(root, width =800, height = 400, bg = '#f0f0fa')
x = 10
y = 20

def foo(step):
        global x,y
        coord = x, y, x + step, y + step
        cv.create_line(coord)
        cv.create_oval(coord)
        x += random.randint(15, 20) + step
        y += random.randint(1, 200) + step
        if x > 800:
                x = random.randint(10, 20)
        if y > 400:
                y = random.randint(15, 29)
        cv.after(500, foo, step)

cv.pack()
#cv.after(500, foo, 10)
thread.start_new_thread(foo, (100,))
thread.start_new_thread(foo, (5,))
thread.start_new_thread(foo, (10,))
mainloop()