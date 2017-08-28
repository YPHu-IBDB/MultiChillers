# -*- coding: utf-8 -*-
from Tkinter import *
import threading
import time
import numpy
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

# 主框架设置
root = Tk()
root.wm_title("建筑空调系统节能软件 V1.0")


# 绘图程序
def draw():
    a = list[1].add_subplot(111)
    t = numpy.arange(0.0, 3.0, 0.01)
    s = numpy.sin(2*numpy.pi*t)
    a.plot(t, s, 'ko-')
    a.xaxis.set_major_formatter()
    list[0].show()

# toolbar = NavigationToolbar2TkAgg(canvas, root)
# toolbar.update()
# canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

# 计时器读取数据
def func():
    print 'hello timer!'
    root.after(2000,func)

def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)

# canvas.mpl_connect('key_press_event', on_key_event)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

# 显示系统当前时间
def display_curtime():
    current = time.strftime("%Y-%m-%d %H:%M:%S")
    Lbl_curtime.configure(text=current)
    root.after(20,display_curtime)

button = Button(root, text='Quit', command=draw)
button.grid()
# button.pack(side=BOTTOM)
Lbl_curtime = Label(root,text='123')
# Lbl_curtime.pack(side = TOP)
Lbl_curtime.grid()

# 建立基本图形窗口
fig = Figure(figsize=(5, 4), dpi=100)
cnv = FigureCanvasTkAgg(fig, master=root)
# cnv.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
cnv.get_tk_widget().grid()
# cnv.grid()
# 用list传递数据到绘图中去
list = [cnv,fig]

# 多线程定时器
threading.Timer(0, func).start()
threading.Timer(0,display_curtime).start()

# 主程序运行
mainloop()

# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.