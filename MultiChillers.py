# -*- coding: utf-8 -*-
from Tkinter import *
# import numpy as np
from numpy import *
import threading
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
# import matplotlib.backends.tkagg as tkagg
# from matplotlib.backends.backend_agg import FigureCanvasAgg

# 定义主框架
root = Tk()
root.title("A figure in a canvas")

# 连接数据库


# 计时器读取数据
def func():
    print 'hello timer!'
    root.after(1000,func)

# 数据的实时更新

# 显示是否有故障数据

# # def draw_figure(canvas, figure, loc=(0, 0)):
# #     """ Draw a matplotlib figure onto a Tk canvas
# #
# #     loc: location of top-left corner of figure on canvas in pixels.
# #
# #     Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
# #     """
# #     figure_canvas_agg = FigureCanvasAgg(figure)
# #     figure_canvas_agg.draw()
# #     figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
# #     canvas = FigureCanvasTkAgg(f, master=root)
# #     canvas.show()
# #     canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
# #
# #     figure_w, figure_h = int(figure_w), int(figure_h)
# #     # photo = PhotoImage(master=canvas, width=figure_w, height=figure_h)
# #
# #     # Position: convert from top-left anchor to center anchor
# #     # canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)
# #     # canvas.grid()
# #     # Unfortunately, there's no accessor for the pointer to the native renderer
# #     tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
# #
# #     # Return a handle which contains a reference to the photo object
# #     # which must be kept live or else the picture disappears
# #     return photo
#
# # Create a canvas
# w, h = 300, 200
# # canvas = tk.Canvas(root, width=w, height=h)
# canvas = Canvas(root)
# canvas.pack()
#
# # Generate some example data
# X = np.linspace(0, 2.0*3.14, 50)
# Y = np.sin(X)
#
# # Create the figure we desire to add to an existing canvas
# fig = mpl.figure.Figure(figsize=(2, 1))
# ax = fig.add_axes([0, 0, 1, 1])
# ax.plot(X, Y)
# canvas = FigureCanvasTkAgg(f, master=root)
# canvas.show()
# canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
# # Keep this handle alive, or else figure will disappear
# # fig_x, fig_y = 100, 100
# # fig_photo = draw_figure(canvas, fig, loc=(fig_x, fig_y))
# # fig_w, fig_h = fig_photo.width(), fig_photo.height()
# #
# # # Add more elements to the canvas, potentially on top of the figure
# # canvas.create_line(200, 50, fig_x + fig_w / 2, fig_y + fig_h / 2)
# # canvas.create_text(200, 50, text="Zero-crossing", anchor="s")



f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
t = arange(0.0, 3.0, 0.01)
s = sin(2*pi*t)

a.plot(t, s)


# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

if __name__ == "__main__":
    # 多线程定时器
    threading.Timer(0, func).start()

    # 主程序运行
    root.mainloop()