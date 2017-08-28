
import threading
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from datetime import *

freqs = np.arange(2, 20, 3)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*freqs[0]*t)
l, = plt.plot(t, s, lw=2)


class Index(object):
    ind = 0

    def next(self, event):
        self.ind += 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

    def prev(self, event):
        self.ind -= 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

callback = Index()
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)

def work():

   print "hello world."


def runTask(func, day=0, hour=0, min=0, second=0):
   # Init time
   now = datetime.now()
   strnow = now.strftime('%Y-%m-%d %H:%M:%S')
   print "now:",strnow
   # First next run time
   period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
   next_time = now + period
   strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
   print "next run:",strnext_time
   while True:
       # Get system current time
       iter_now = datetime.now()
       iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
       if str(iter_now_time) == str(strnext_time):
           # Get every start work time
           print "start work: %s" % iter_now_time
           # Call task func
           func()
           print "task done."
           # Get next iteration time
           iter_time = iter_now + period
           strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
           print "next_iter: %s" % strnext_time
           # Continue next iteration
           continue



# plt.show()
# runTask(work, min=0.5)
# runTask(work, day=0, hour=0, min=0, second=2)
runTask(plt.show(),second=2)
