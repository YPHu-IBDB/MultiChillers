# -*- coding: utf-8 -*-
import Tkinter as tk
import time

def update_timeText():
# Get the current time, note you can change the format as you wish
    current = time.strftime("%H:%M:%S")
# Update the timeText Label box with the current time
    timeText.configure(text=current)
# Call the update_timeText() function after 1 second

def update():
    root.after(2000, update_timeText)

root = tk.Tk()
root.wm_title("Simple Clock Example")

# Create a timeText Label (a text box)
timeText = tk.Label(root, text="", font=("Helvetica", 150))
timeText.pack()
update_timeText()
update()
# while True:
#     current = time.strftime("%H:%M:%S")
#     timeText.configure(text=current)
#     # time.sleep(2)
#     root.after(2000, update_timeText)

root.mainloop()